"""Mosyle Manager - Classes"""
import json
import math
import os
import uuid

import click
import requests
from requests.auth import HTTPBasicAuth

from mosyle.api import REQUEST_HEADERS, REQUEST_URL
from mosyle.configuration.config import Config

from .api import ApiClient
from .configuration.config import Config

HOME = os.path.expanduser("~")
MOSYLE_DIR = f"{HOME}/.mosyle"

CONFIG = Config()
session = requests.Session()
session.headers.update(REQUEST_HEADERS)
session.auth = HTTPBasicAuth(CONFIG.username, CONFIG.password)


# CSVs
def write_csv():
    pass


def read_csv():
    pass


# Request Builders
def post_build():
    pass


def get_build():
    pass


def put_build():
    pass


def patch_build():
    pass


def delete_build():
    pass


# Request
def request():
    click.echo("Requesting...")


# Cache
def get_page_count():
    payload = {
        "accessToken": CONFIG.token,
    }
    response = session.post(f"{REQUEST_URL}/listclasses", json=payload).json()[
        "response"
    ]
    total: int = response["total"]
    page_size: int = response["page_size"]
    return math.ceil(int(total) // page_size)


def get_pager():  # sourcery skip: remove-unnecessary-cast
    payload = {
        "accessToken": CONFIG.token,
        "options": {
            "page": 1,
            "specific_columns": [
                "id",
                "class_name",
                "course_name",
                "location",
                "teacher",
                "students",
                "coordinators",
            ],
        },
    }
    response = session.post(f"{REQUEST_URL}/listclasses", json=payload).json()[
        "response"
    ]
    total: int = response["total"]
    page_size: int = response["page_size"]
    page_count: int = math.ceil(int(total) // page_size)
    yield response

    for page_num in range(1, page_count + 2):
        payload = {
            "accessToken": CONFIG.token,
            "options": {
                "page": page_num,
                "specific_columns": [
                    "id",
                    "class_name",
                    "course_name",
                    "location",
                    "teacher",
                    "students",
                    "coordinators",
                ],
            },
        }
        yield session.post(f"{REQUEST_URL}/listclasses", json=payload).json()[
            "response"
        ]


def refresh_cache():
    click.echo("Refreshing Cache...")
    classes: list[object] = []

    with click.progressbar(get_pager(), length=get_page_count()) as pager:
        for page in pager:
            classes = [*classes, *page["classes"]]

    classes_json = json.dumps(classes, indent=4)
    with open(f"{MOSYLE_DIR}/classes.json", "w", encoding="UTF-8") as outfile:
        outfile.write(classes_json)


def update_cache():
    click.echo("Updating Cache...")


def validate_cache():
    click.echo("Validating Cache...")
    # Test File Path
    # Check Time Stamp
    # If expired, then refresh
    refresh_cache()


def validate_options():
    click.echo("Validating Options...")


def build_request():
    click.echo("Building Request...")


def prompt_approval():
    click.echo("Prompting Approval...")


def display_response():
    click.echo("Displaying Response...")


# Click CLI


@click.group()
def classes():
    pass


OPTIONS = [
    ("-s", "--course-name", "Course Name"),
    ("-n", "--class-name", "Class Name"),
    ("-l", "--location", "Location"),
    ("-t", "--teacher-id", "Teacher User ID"),
    ("-R", "--room", "Room"),
    ("-p", "--platform", "Platform"),
    ("-c", "--coordinators", "Coordinators User ID [id1,id2]"),
    ("-s", "--students", "Students User ID [id1,id2]"),
    ("-r", "--roster", "Class Roster CSV (Role, User ID)"),
]


@classes.command()
@click.option("-s", "--course-name", prompt=True, required=True, help="Course Name")
@click.option("-n", "--class-name", prompt=True, required=True, help="Class Name")
@click.option("-l", "--location", prompt=True, required=True, help="Location")
@click.option("-t", "--teacher-id", prompt=True, required=True, help="Teacher User ID")
@click.option("-R", "--room", help="Room")
@click.option("-p", "--platform", help="Platform")
@click.option("-c", "--coordinators", help="Coordinators User ID [id1,id2]")
@click.option("-s", "--students", help="Students User ID [id1,id2]")
@click.option("-r", "--roster", help="Class Roster CSV (Role, User ID)")
def post(
    course_name: str,
    class_name: str,
    location: str,
    teacher_id: str,
    room: str,
    platform: str,
    coordinators: str,
    students: str,
    roster: str,
):
    validate_cache()
    validate_options()
    build_request()
    prompt_approval()
    request()
    display_response()
    update_cache()


@classes.command()
def get():
    validate_cache()
    validate_options()
    request()
    display_response()


@classes.command()
def put():
    validate_cache()
    validate_options()
    build_request()
    prompt_approval()
    request()
    display_response()
    update_cache()


@classes.command()
def patch():
    validate_cache()
    validate_options()
    build_request()
    prompt_approval()
    request()
    display_response()
    update_cache()


@classes.command()
def delete():
    validate_cache()
    validate_options()
    build_request()
    prompt_approval()
    request()
    display_response()
    update_cache()


class Classes:
    """Classes"""

    @staticmethod
    def post(
        course_name: str,
        class_name: str,
        location: str,
        teacher_id: str,
        students: list[str] | None = None,
        room: str | None = None,
        coordinators: list[str] | None = None,
        platform: str | None = None,
    ):
        """Section Operations"""

        payload: dict[str, object] = {
            "accessToken": CONFIG.token,
        }

        element: dict[str, object] = {
            "operation": "save",
            "id": str(uuid.uuid4()),
            "course_name": course_name,
            "class_name": class_name,
            "location": location,
            "idteacher": teacher_id,
        }
        if students is not None:
            element["students"] = students
        if room is not None:
            element["room"] = room
        if coordinators is not None:
            element["coordinators"] = coordinators
        if platform is not None:
            element["platform"] = platform

        payload["elements"] = [element]

        response = session.post(f"{REQUEST_URL}/classes", json=payload).json()

        # print(json.dumps(payload, indent=4))
        # print(json.dumps(response, indent=4))

        return response

    @staticmethod
    def get_pager():  # sourcery skip: remove-unnecessary-cast
        pass

    @staticmethod
    def put(
        api_client: ApiClient,
        class_id: str,
        course_name: str,
        class_name: str,
        location: str,
        id_teacher: str,
        students: list[str] | None = None,
        room: str | None = None,
        coordinators: list[str] | None = None,
        platform: str | None = None,
    ):
        """Section Operations"""
        element: dict[str, object] = {
            "id": class_id,
            "operation": "save",
            "course_name": course_name,
            "class_name": class_name,
            "location": location,
            "idteacher": id_teacher,
        }
        if students is not None:
            element["students"] = students
        if room is not None:
            element["room"] = room
        if coordinators is not None:
            element["coordinators"] = coordinators
        if platform is not None:
            element["platform"] = platform
        return api_client.post("", elements=[element])

    @staticmethod
    def patch(
        api_client: ApiClient,
        class_id: str,
        course_name: str,
        class_name: str,
        location: str,
        id_teacher: str,
        students: list[str] | None = None,
        room: str | None = None,
        coordinators: list[str] | None = None,
        platform: str | None = None,
    ):
        """Section Operations"""
        element: dict[str, object] = {
            "id": class_id,
            "operation": "save",
            "course_name": course_name,
            "class_name": class_name,
            "location": location,
            "idteacher": id_teacher,
        }
        if students is not None:
            element["students"] = students
        if room is not None:
            element["room"] = room
        if coordinators is not None:
            element["coordinators"] = coordinators
        if platform is not None:
            element["platform"] = platform
        return api_client.post("", elements=[element])

    @staticmethod
    def delete():
        pass


'''
Class Cli:
    """Classes CLI"""

    @click.group()
    @staticmethod
    def classes():
        """Classes"""

    @classes.command()
    @click.option("-c", "--course-name", required=True, help="Course Name")
    @click.option("-n", "--class-name", required=True, help="Class Name")
    @click.option("-l", "--location", required=True, help="Location")
    @click.option("-t", "--teacher-id", required=True, help="Teacher User ID")
    @click.option("-R", "--room", required=False, help="Room")
    # @click.option(
    #    "-C", "--coordinators", required=False, help="Array of Coordinator IDs"
    # )
    @click.option(
        "-p",
        "--platform",
        required=False,
        help="Platform Name (default ios)",
        type=click.Choice(["ios", "mac"]),
    )
    # @click.option("-s", "--students", required=False, help="Array of Student IDs")
    # @click.option(
    #    "-r",
    #    "--roster",
    #    required=False,
    #    help="Filepath to New Class Roster CSV (list of user IDs, class role). -s is ignored if this is provided.",
    # )
    @staticmethod
    def post(
        course_name: str,
        class_name: str,
        location: str,
        teacher_id: str,
        room: str | None = None,
        # coordinators: list[str] | None = None,
        platform: str | None = None,
        # students: list[str] | None = None,
        # roster_file: str | None = None,
    ):
        """Create Classes"""
        new_class: dict[str, str] = Classes.post(
            course_name=course_name,
            class_name=class_name,
            location=location,
            teacher_id=teacher_id,
            room=room,
            # coordinators=coordinators,
            platform=platform,
            # students=students,
        )
        click.echo(new_class)

    @classes.command()
    @click.option("-id", "--guid", help="Filepath write Classes CSV.")
    @click.option("-cc", "--classes-csv", help="Filepath write Classes CSV.")
    @click.option("-rc", "--rosters-csv", help="Filepath write Rosters CSV.")
    @staticmethod
    def get(cc: str, rc: str):
        """Read Classes"""
        classes: list[object] = Classes.get()
        click.echo(f"{len(classes)} Classes Retrieved")

    @classes.command()
    @staticmethod
    def put():
        """Replace Classes"""
        click.echo("Not Implemented")

    @classes.command()
    @staticmethod
    def patch():
        """Modify Classes"""
        click.echo("Not Implemented")

    @classes.command()
    @staticmethod
    def delete():
        """Delete Classes"""
        click.echo("Not Implemented")


if __name__ == "__main__":
    Cli.classes()
'''
