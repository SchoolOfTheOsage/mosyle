import requests

from .. import HEADERS, URL
from .attributes import Attributes
from .platforms import Platforms


class Devices:
    def __init__(self):
        self.devices: list[dict[str, str]] = []

    def read(
        self,
        access_token: str,
        platform: Platforms,
        tags: list[str] | None = None,
        os_versions: list[str] | None = None,
        serial_numbers: list[str] | None = None,
        page: int | None = None,
        attributes: Attributes | None = None,
    ):
        headers = HEADERS.copy()

        options = {
            "os": platform.value,
        }
        if tags is not None:
            options["tags"] = tags
        if os_versions is not None:
            options["osversions"] = os_versions
        if serial_numbers is not None:
            options["serial_numbers"] = serial_numbers
        if attributes is not None:
            options["specific_columns"] = attributes.to_strings()
        if page is not None:
            options["page"] = page
        payload = {
            "accessToken": access_token,
            "options": options,
        }
        response = requests.post(
            URL + "/listdevices", json=payload, timeout=60, headers=headers
        )
        self.devices = response.json()["response"]["devices"]

    def read_group_by_id(
        self,
        group_id: str,
        access_token: str,
        platform: Platforms,
        tags: list[str] | None = None,
        os_versions: list[str] | None = None,
        serial_numbers: list[str] | None = None,
        page: int | None = None,
        attributes: Attributes | None = None,
    ):
        pass

    def read_group_by_name(
        self,
        name: str,
        access_token: str,
        platform: Platforms,
        tags: list[str] | None = None,
        os_versions: list[str] | None = None,
        serial_numbers: list[str] | None = None,
        page: int | None = None,
        attributes: Attributes | None = None,
    ):
        headers = HEADERS.copy()

        options = {
            "os": platform.value,
        }
        payload = {
            "accessToken": access_token,
            "options": options,
        }
        response = requests.post(
            URL + "/listdevicegroups", json=payload, timeout=60, headers=headers
        )
        groups = dict(
            [
                (group["name"], group["id"])
                for group in response.json()["response"]["groups"]
            ]
        )
        group_id = groups[name]
        self.read_group_by_id(
            access_token=access_token,
            group_id=group_id,
            platform=platform,
            tags=tags,
            os_versions=os_versions,
            serial_numbers=serial_numbers,
            page=page,
            attributes=attributes,
        )

    def update(self):
        pass

    def delete(self):
        pass

    def erase(self):
        pass

    def restart(self):
        pass

    def shutdown(self):
        pass

    def clear_commands(self):
        pass

    def clear_pending_commands(self):
        pass

    def clear_failed_commands(self):
        pass

    def change_to_limbo(self):
        pass

    def enable_lost_mode(self):
        pass

    def disable_lost_mode(self):
        pass

    def play_sound(self):
        pass

    def request_location(self):
        pass
