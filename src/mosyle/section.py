"""Mosyle Manager Python API - Section (Class)"""
from dataclasses import dataclass

import click

from .api_client import ApiClient
from .click_order_commands import OrderCommands
from .str_enum import StrEnum


class SectionApiResource(StrEnum):
    """Section API Resource Enumeration"""

    GET = "listclasses"
    OPERATION = "classes"


class SectionColumn(StrEnum):
    """Class Column Enumeration"""

    ID = "id"
    SECTION_NAME = "class_name"
    SUBJECT_NAME = "course_name"
    LOCATION = "location"
    TEACHER = "teacher"
    STUDENTS = "students"
    COORDINATORS = "coordinators"
    ACCOUNT = "account"


class SectionOperation(StrEnum):
    """Class Operation Enumeration"""

    SAVE = "save"
    DELETE = "delete"


class SectionPlatform(StrEnum):
    """Class Platform Enumeration"""

    IOS = "ios"
    MACOS = "mac"


@dataclass(frozen=True, slots=True)
class Section:
    """Section"""

    def get(
        self,
        page: int | None = None,
        specific_columns: list[SectionColumn] | None = None,
    ):
        """List Sections"""

        options = {}
        if page is not None:
            options["page"] = page
        if specific_columns is not None:
            options["specific_columns"] = specific_columns

        # return self.post(Endpoint.LIST_CLASSES, options=options)

    def operation(
        self,
        class_id: str,
        operation: SectionOperation,
        course_name: str,
        class_name: str,
        location: str,
        id_teacher: str,
        students: list[str] | None = None,
        room: str | None = None,
        coordinators: list[str] | None = None,
        platform: SectionPlatform | None = None,
    ):
        """Section Operations"""

        element: dict[str, object] = {
            "id": class_id,
            "operation": operation,
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

        # return self.post(Endpoint.CLASSES, elements=[element])


class SectionCli:
    """Section CLI"""

    @click.group(cls=OrderCommands)
    @staticmethod
    def section():
        """Sections"""
        click.echo("Not Implemented")

    @section.command()
    @staticmethod
    def create():
        """Create"""
        click.echo("Not Implemented")

    @section.command()
    @staticmethod
    def read():
        """Read"""
        click.echo("Not Implemented")

    @section.command()
    @staticmethod
    def update():
        """Update"""
        click.echo("Not Implemented")

    @section.command()
    @staticmethod
    def delete():
        """Delete"""
        click.echo("Not Implemented")


if __name__ == "__main__":
    SectionCli.section()
