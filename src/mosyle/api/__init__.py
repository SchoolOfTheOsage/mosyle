"""Mosyle API"""

import requests
from requests.auth import HTTPBasicAuth

from .account_operation import AccountOperation
from .cisco_ise_operation import CiscoIseOperation
from .class_column import ClassColumn
from .class_operation import ClassOperation
from .class_platform import ClassPlatform
from .device_column import DeviceColumn
from .device_lost_mode_operation import DeviceLostModeOperation
from .device_operation import DeviceOperation
from .device_platform import DevicePlatform
from .user_column import UserColumn
from .user_list_type import UserListType
from .user_operation import UserOperation
from .user_operation_type import UserOperationType

REQUEST_URL: str = "https://managerapi.mosyle.com/v2"
REQUEST_HEADERS = {
    "content-type": "application/json",
}
REQUEST_TIMEOUT: int = 60


class Api:
    """Mosyle API"""

    def __init__(
        self,
        access_token: str,
        username: str | None = None,
        password: str | None = None,
    ):
        self.access_token = access_token
        if username is not None and password is not None:
            self.auth = HTTPBasicAuth(username, password)
        else:
            self.auth = None

    # pylint: disable=too-many-arguments
    def list_devices(
        self,
        device_platform: DevicePlatform,
        tags: list[str] | None = None,
        os_versions: list[str] | None = None,
        serial_numbers: list[str] | None = None,
        page: int | None = None,
        specific_columns: list[DeviceColumn] | None = None,
    ):
        """List Devices"""
        url = f"{REQUEST_URL}/listdevices"

        options: dict[str, DevicePlatform | list[str] | int | list[DeviceColumn]] = {
            "os": device_platform,
        }
        if tags is not None:
            options["tags"] = tags
        if os_versions is not None:
            options["osversions"] = os_versions
        if serial_numbers is not None:
            options["serial_numbers"] = serial_numbers
        if page is not None:
            options["page"] = page
        if specific_columns is not None:
            options["specific_columns"] = specific_columns

        payload: dict[str, object] = {
            "accessToken": self.access_token,
            "options": options,
        }

        return requests.post(
            url,
            json=payload,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
        ).json()

    def devices(
        self,
        serial_number: str,
        asset_tag: str | None = None,
        tags: str | None = None,
        name: str | None = None,
        lock: str | None = None,
    ):
        """Update Device Attributes"""
        url = f"{REQUEST_URL}/devices"

        element: dict[str, object] = {
            "serialnumber": serial_number,
        }
        if asset_tag is not None:
            element["asset_tag"] = asset_tag
        if tags is not None:
            element["tags"] = tags
        if name is not None:
            element["name"] = name
        if lock is not None:
            element["lock"] = lock

        payload = {
            "accessToken": self.access_token,
            "elements": [element],
        }

        requests.post(
            url,
            json=payload,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
            auth=self.auth,
        ).json()

    def bulk_operations(
        self,
        operation: DeviceOperation,
        device_udids: list[str] | None = None,
        group_ids: list[str] | None = None,
        pin_code: str | None = None,
        preserve_data_plan: bool | None = None,
        disallow_proximity_setup: bool | None = None,
        revoke_vpp_license: bool | None = None,
    ) -> dict[str, object]:
        """Device Bulk Operations"""
        url = f"{REQUEST_URL}/bulkops"

        element: dict[str, object] = {
            "operation": operation,
        }
        if device_udids is not None:
            element["devices"] = device_udids
        if group_ids is not None:
            element["groups"] = group_ids

        options: dict[str, object] = {}
        if pin_code is not None:
            options["pin_code"] = pin_code
        if preserve_data_plan is not None:
            options["PreserveDataPlan"] = preserve_data_plan
        if disallow_proximity_setup is not None:
            options["DisallowProximitySetup"] = disallow_proximity_setup
        if revoke_vpp_license is not None:
            options["RevokeVPPLicenses"] = revoke_vpp_license
        if options:
            element["options"] = options

        payload = {
            "accessToken": self.access_token,
            "elements": [element],
        }

        return requests.post(
            url,
            json=payload,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
            auth=self.auth,
        ).json()

    def lost_mode(
        self,
        operation: DeviceLostModeOperation,
        device_udids: list[str] | None = None,
        group_ids: list[str] | None = None,
        message: str | None = None,
        phone_number: str | None = None,
        footnote: str | None = None,
    ):
        """Device Lost Mode Operations"""
        url = f"{REQUEST_URL}/lostmode"

        element: dict[str, object] = {
            "operation": operation,
        }
        if device_udids is not None:
            element["devices"] = device_udids
        if group_ids is not None:
            element["groups"] = group_ids
        if message is not None:
            element["message"] = message
        if phone_number is not None:
            element["phone_number"] = phone_number
        if footnote is not None:
            element["footnote"] = footnote

        payload = {
            "accessToken": self.access_token,
            "elements": [element],
        }

        return requests.post(
            url,
            json=payload,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
            auth=self.auth,
        ).json()

    def list_users(
        self,
        page: int | None = None,
        specific_columns: list[UserColumn] | None = None,
        types: list[UserListType] | None = None,
    ):
        """List Users"""
        url = f"{REQUEST_URL}/listusers"

        options: dict[str, object] = {}
        if page is not None:
            options["page"] = page
        if specific_columns is not None:
            options["specific_columns"] = specific_columns
        if types is not None:
            options["types"] = types

        payload: dict[str, object] = {
            "accessToken": self.access_token,
        }
        if options:
            payload["options"] = options

        return requests.post(
            url,
            json=payload,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
        ).json()

    def users(
        self,
        user_id: str,
        operation: UserOperation,
        name: str | None = None,
        user_type: UserOperationType | None = None,
        email: str | None = None,
        managed_apple_id: str | None = None,
        locations: list[tuple[str, str]]
        | None = None,  # List of tuples of (location_name, grade_level)
        welcome_email: bool | None = None,
        serial_number: str | None = None,
    ):
        """User Operations"""
        url = f"{REQUEST_URL}/users"

        element: dict[str, object] = {
            "id": user_id,
            "operation": operation,
        }
        if name is not None:
            element["name"] = name
        if user_type is not None:
            element["type"] = user_type
        if email is not None:
            element["email"] = email
        if managed_apple_id is not None:
            element["managed_appleid"] = managed_apple_id
        if locations is not None:
            element["locations"] = locations
        if welcome_email is not None:
            element["welcome_email"] = welcome_email
        if serial_number is not None:
            element["serial_number"] = serial_number

        payload = {
            "accessToken": self.access_token,
            "elements": [element],
        }

        return requests.post(
            url,
            json=payload,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
            auth=self.auth,
        ).json()

    def classes(
        self,
        class_id: str,
        operation: ClassOperation,
        course_name: str,
        class_name: str,
        location: str,
        id_teacher: str,
        students: list[str] | None = None,
        room: str | None = None,
        coordinators: list[str] | None = None,
        platform: ClassPlatform | None = None,
    ):
        """Class Operations"""
        url = f"{REQUEST_URL}/classes"

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
        payload = {
            "accessToken": self.access_token,
            "elements": [element],
        }

        return requests.post(
            url,
            json=payload,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
            auth=self.auth,
        ).json()

    def list_classes(
        self,
        page: int | None = None,
        specific_columns: list[ClassColumn] | None = None,
    ):
        """List Classes"""
        url = f"{REQUEST_URL}/listclasses"

        options = {}
        if page is not None:
            options["page"] = page
        if specific_columns is not None:
            options["specific_columns"] = specific_columns
        payload: dict[str, object] = {
            "accessToken": self.access_token,
        }

        if options:
            payload["options"] = options

        return requests.post(
            url,
            json=payload,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
        ).json()

    def accounts(
        self,
        operation: AccountOperation | None = None,
        school_name: str | None = None,
        school_address: str | None = None,
        leader_name: str | None = None,
        leader_email: str | None = None,
        leader_id: str | None = None,
        uuid: str | None = None,
    ):
        """Account Operations"""
        url = f"{REQUEST_URL}/accounts"

        payload = {
            "accessToken": self.access_token,
        }
        if operation is not None:
            payload["operation"] = operation
        if school_name is not None:
            payload["school_name"] = school_name
        if school_address is not None:
            payload["school_address"] = school_address
        if leader_name is not None:
            payload["leader_name"] = leader_name
        if leader_email is not None:
            payload["leader_email"] = leader_email
        if leader_id is not None:
            payload["leader_id"] = leader_id
        if uuid is not None:
            payload["uuid"] = uuid

        auth = self.auth if operation == AccountOperation.REQUEST else None

        return requests.post(
            url,
            json=payload,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
            auth=auth,
        ).json()

    def cisco_ise(
        self,
        action: CiscoIseOperation,
        wifimac: str,
        serialnumber: str,
        model: str | None = None,
    ):
        """Cisco ISE Operations"""
        url = f"{REQUEST_URL}/ciscoise"

        element: dict[str, object] = {
            "action": action,
            "wifimac": wifimac,
            "serialnumber": serialnumber,
        }

        if model is not None:
            element["model"] = model

        payload = {
            "accessToken": self.access_token,
            "elements": [element],
        }

        return requests.post(
            url,
            json=payload,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
            auth=self.auth,
        ).json()

    def get_cisco_ise(self, paging: int):
        """Get Cisco ISE"""
        url = f"{REQUEST_URL}/getciscoise"

        payload = {
            "accessToken": self.access_token,
            "paging": paging,
        }

        return requests.post(
            url,
            json=payload,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
            auth=self.auth,
        ).json()

    def list_device_groups(
        self,
        device_platform: DevicePlatform,
        page: int | None = None,
    ) -> dict[str, object]:
        """List Device Groups"""
        url = f"{REQUEST_URL}/listdevicegroups"

        options: dict[str, object] = {
            "os": device_platform,
        }

        if page is not None:
            options["page"] = page

        payload = {
            "accessToken": self.access_token,
            "options": options,
        }

        return requests.post(
            url,
            json=payload,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
        ).json()

    def list_devices_by_group(
        self,
        device_group_id: str,
    ) -> dict[str, object]:
        """List Devices By Group"""
        url = f"{REQUEST_URL}/listdevicesbygroup"

        options = {
            "iddevicegroup": device_group_id,
        }

        payload = {
            "accessToken": self.access_token,
            "options": options,
        }

        return requests.post(
            url,
            json=payload,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
        ).json()

    def adminlogs(
        self,
        page: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        id_users: list[str] | None = None,
    ):
        """Administrative Action Logs"""
        url = f"{REQUEST_URL}/actions"

        filter_options: dict[str, object] = {}
        if start_date is not None:
            filter_options["start_date"] = start_date
        if end_date is not None:
            filter_options["end_date"] = end_date
        if id_users is not None:
            filter_options["idusers"] = id_users

        payload: dict[str, object] = {
            "accessToken": self.access_token,
        }

        if page is not None:
            payload["page"] = page

        if filter_options:
            payload["filter_options"] = filter_options

        return requests.post(
            url,
            json=payload,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
        ).json()
