from ..api import ApiClient
from ..str_enum import StrEnum
from .column import Column
from .lostmode_operation import LostModeOperation
from .operation import Operation
from .platform import Platform


class ApiResource(StrEnum):
    """Device API Resource Enumeration"""

    GET = "listdevices"
    OPERATION = "devices"
    BULK_OPERATION = "bulkops"
    LOST_MODE_OPERATION = "lostmode"
    GET_GROUPS = "listdevicegroups"
    GET_BY_GROUP = "listdevicesbygroup"


def get(
    api_client: ApiClient,
    device_platform: Platform,
    tags: list[str] | None = None,
    os_versions: list[str] | None = None,
    serial_numbers: list[str] | None = None,
    page: int | None = None,
    specific_columns: list[Column] | None = None,
):
    """Get Devices"""
    options: dict[str, object] = {
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
    return api_client.post(ApiResource.GET, options=options)


def get_by_group(
    api_client: ApiClient,
    device_group_id: str,
):
    """Get Devices By Group"""
    options: dict[str, object] = {
        "iddevicegroup": device_group_id,
    }
    return api_client.post(ApiResource.GET_BY_GROUP, options=options)


def update(
    api_client: ApiClient,
    serial_number: str,
    asset_tag: str | None = None,
    tags: list[str] | None = None,
    device_name: str | None = None,
    lock_message: str | None = None,
):
    """Update Device Attributes"""
    element: dict[str, object] = {
        "serialnumber": serial_number,
    }
    if asset_tag is not None:
        element["asset_tag"] = asset_tag
    if tags is not None:
        # FIXME: convert tags from list to comma separated string
        element["tags"] = tags
    if device_name is not None:
        element["name"] = device_name
    if lock_message is not None:
        element["lock"] = lock_message
    return api_client.post(ApiResource.OPERATION, elements=[element])


def bulk_operation(
    api_client: ApiClient,
    operation: Operation,
    device_udids: list[str] | None = None,
    group_ids: list[str] | None = None,
    pin_code: str | None = None,
    preserve_data_plan: bool | None = None,
    disallow_proximity_setup: bool | None = None,
    revoke_vpp_license: bool | None = None,
) -> dict[str, object]:
    """Devices Bulk Operation"""

    element: dict[str, object] = {
        "operation": operation,
    }
    if device_udids is not None:
        element["devices"] = device_udids
    if group_ids is not None:
        element["groups"] = group_ids
    options: dict[str, str | bool] = {}
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

    return api_client.post(ApiResource.BULK_OPERATION, elements=[element])


def lost_mode_operation(
    api_client: ApiClient,
    operation: LostModeOperation,
    device_udids: list[str] | None = None,
    group_ids: list[str] | None = None,
    message: str | None = None,
    phone_number: str | None = None,
    footnote: str | None = None,
) -> dict[str, object]:
    """Devices Lost Mode Operation"""
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
    return api_client.post(ApiResource.LOST_MODE_OPERATION, elements=[element])


def get_groups(
    api_client: ApiClient,
    device_platform: Platform,
    page: int | None = None,
) -> dict[str, object]:
    """Get Device Groups"""
    options: dict[str, object] = {
        "os": device_platform,
    }
    if page is not None:
        options["page"] = page
    return api_client.post(ApiResource.GET_GROUPS, options=options)
