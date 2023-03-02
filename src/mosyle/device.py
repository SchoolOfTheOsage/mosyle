"""Mosyle Manager Python API - Device"""
import dataclasses
from dataclasses import dataclass

import click

from .api_client import ApiClient
from .click_order_commands import OrderCommands
from .str_enum import StrEnum


class ApiResource(StrEnum):
    """Device API Resource Enumeration"""

    GET = "listdevices"
    OPERATION = "devices"
    BULK_OPERATION = "bulkops"
    LOST_MODE_OPERATION = "lostmode"
    GET_GROUPS = "listdevicegroups"
    GET_BY_GROUP = "listdevicesbygroup"


class Column(StrEnum):
    """Device Column Enumeration"""

    DEVICE_UDID = "deviceudid"
    TOTAL_DISK = "total_disk"
    OPERATING_SYSTEM = "os"
    SERIAL_NUMBER = "serial_number"
    DEVICE_NAME = "device_name"
    DEVICE_MODEL = "device_model"
    BATTERY = "battery"
    OS_VERSION = "osversion"
    DATE_INFO = "date_info"
    CARRIER = "carrier"
    ROAMING_ENABLED = "roaming_enabled"
    IS_ROAMING = "isroaming"
    IMEI = "imei"
    MEID = "meid"
    AVAILABLE_DISK = "available_disk"
    WIFI_MAC_ADDRESS = "wifi_mac_address"
    LAST_IP_BEAT = "last_ip_beat"
    LAST_LAN_IP = "last_lan_ip"
    BLUETOOTH_MAC_ADDRESS = "bluetooth_mac_address"
    IS_SUPERVISED = "is_supervised"
    DATE_APP_INFO = "date_app_info"
    DATE_LAST_BEAT = "date_last_beat"
    DATE_LAST_PUSH = "date_last_push"
    STATUS = "status"
    IS_ACTIVATION_LOCK_ENABLED = "isActivationLockEnabled"
    IS_DEVICE_LOCATOR_SERVICE_ENABLED = "isDeviceLocatorServiceEnabled"
    IS_DO_NOT_DISTURB_IN_EFFECT = "isDoNotDisturbInEffect"
    IS_CLOUD_BACKUP_ENABLED = "isCloudBackupEnabled"
    IS_NETWORK_TETHERED = "IsNetworkTethered"
    NEED_OS_UPDATE = "needosupdate"
    PRODUCT_KEY_UPDATE = "productkeyupdate"
    DEVICE_TYPE = "device_type"
    LOSTMODE_STATUS = "lostmode_status"
    IS_MUTED = "is_muted"
    DATE_MUTED = "date_muted"
    ACTIVATION_BYPASS = "activation_by"
    DATE_MEDIA_INFO = "date_media_info"
    TAGS = "tags"
    ITUNES_STORE_ACCOUNT_HASH = "iTunesStoreAccountHash"
    ITUNES_STORE_ACCOUNT_IS_ACTIVE = "iTunesStoreAccountIsActive"
    DATE_PROFILES_INFO = "date_profiles_info"
    ETHERNET_MAC_ADDRESS = "ethernet_mac_address"
    MODEL_NAME = "model_name"
    LAST_CLOUD_BACKUP_DATE = "LastCloudBackupDate"
    SYSTEM_INTEGRITY_PROTECTION_ENABLED = "SystemIntegrityProtectionEnabled"
    BUILD_VERSION = "BuildVersion"
    LOCAL_HOST_NAME = "LocalHostName"
    HOST_NAME = "HostName"
    OS_UPDATE_SETTINGS = "OSUpdateSettings"
    ACTIVE_MANAGED_USERS = "ActiveManagedUsers"
    CURRENT_CONSOLE_MANAGED_USER = "CurrentConsoleManagedUser"
    DATE_PRINTERS = "date_printers"
    AUTO_SETUP_ADMIN_ACCOUNTS = "AutoSetupAdminAccounts"
    APPLE_TV_ID = "appleTVid"
    ASSET_TAG = "asset_tag"
    MANAGEMENT_STATUS = "ManagementStatus"
    OS_UPDATE_STATUS = "OSUpdateStatus"
    AVAILABLE_OS_UPDATES = "AvailableOSUpdates"
    ENROLLMENT_TYPE = "enrollment_type"
    USER_ID = "userid"
    USER_NAME = "username"
    USER_TYPE = "usertype"
    SHARED_CART_NAME = "SharedCartName"
    DEVICE_MODEL_NAME = "device_model_name"
    DATE_KINFO = "date_kinfo"
    LOCATION = "location"
    LATITUDE = "latitude"
    LONGITUDE = "longitude"


class LostModeOperation(StrEnum):
    """Device Lost Mode Operation Enumeration"""

    ENABLE = "enable"
    DISABLE = "disable"
    PLAY_SOUND = "play_sound"
    REQUEST_LOCATION = "request_location"


class Operation(StrEnum):
    """Device Operation Enumeration"""

    WIPE = "wipe_devices"
    RESTART = "restart_devices"
    SHUTDOWN = "shutdown_devices"
    CLEAR_COMMANDS = "clear_commands"
    CLEAR_PENDING_COMMANDS = "clear_pending_commands"
    CLEAR_FAILED_COMMANDS = "clear_failed_commands"
    UNASSIGN = "change_to_limbo"


class Platform(StrEnum):
    """Device Platform Enumeration"""

    IOS = "ios"
    MACOS = "macos"
    TVOS = "tvos"


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


@dataclass(frozen=True, slots=True)
class Device:
    """Device"""

    _api_client: ApiClient
    _attributes: dict[str, object]
    device_uuid: str
    total_disk: str
    operating_system: str
    serial_number: str
    device_name: str
    device_model: str
    battery: str
    os_version: str
    date_info: str
    carrier: str
    roaming_enabled: str
    is_roaming: str
    imei: str
    meid: str
    available_disk: str
    wifi_mac_address: str
    last_ip_beat: str
    last_lan_ip: str
    bluetooth_mac_address: str
    is_supervised: str
    date_app_info: str
    date_last_beat: str
    date_last_push: str
    status: str
    is_activation_lock_enabled: str
    is_device_locator_service_enabled: str
    is_do_not_disturb_in_effect: str
    is_cloud_backup_enabled: str
    is_network_tethered: str
    need_os_update: str
    product_key_update: str
    device_type: str
    lostmode_status: str
    is_muted: str
    date_muted: str
    activation_by: str
    date_media_info: str
    _tags: list[str]
    itunes_store_account_hash: str
    itunes_store_account_is_active: str
    date_profiles_info: str
    ethernet_mac_address: str
    model_name: str
    last_cloud_backup_date: str
    system_integrity_protection_enabled: str
    build_version: str
    local_host_name: str
    host_name: str
    os_update_settings: str
    active_managed_users: str
    current_console_managed_user: str
    date_printers: str
    auto_setup_admin_accounts: str
    apple_tv_id: str
    _asset_tag: str
    management_status: str
    os_update_status: str
    available_os_updates: str
    enrollment_type: str
    user_id: str
    user_name: str
    user_type: str
    shared_cart_name: str
    device_model_name: str
    date_kinfo: str
    location: str
    latitude: str
    longitude: str

    def __post_init__(self):
        pass

    def get(self, device_platform: Platform, serial_number: str):
        """Get Device"""

        # FIXME: save returned device attributes to self attributes.
        # See Dacite library. https://github.com/konradhalas/dacite
        get(
            self._api_client,
            device_platform=device_platform,
            serial_numbers=[serial_number],
        )

    def refresh(self):
        """Refresh Device"""
        get(
            self._api_client,
            device_platform=Platform[self.operating_system],
            serial_numbers=[self.serial_number],
        )

    @property
    def asset_tag(self) -> str:
        """Device Asset Tag"""
        return self._asset_tag

    @asset_tag.setter
    def asset_tag(self, asset_tag: str):
        """Set Device Asset Tag"""
        update(self._api_client, self.serial_number, asset_tag=asset_tag)
        dataclasses.replace(self, _asset_tag=asset_tag)

    @property
    def name(self) -> str:
        """Device Name"""
        return self.device_name

    @name.setter
    def name(self, device_name: str):
        """Set Device Name"""
        update(self._api_client, self.serial_number, device_name=device_name)
        dataclasses.replace(self, device_name=device_name)

    def set_lock(self, message: str):
        """Set Device Lock Screen Message"""
        update(self._api_client, self.serial_number, lock_message=message)

    @property
    def tags(self) -> list[str]:
        """Device Tags"""
        return self._tags

    @tags.setter
    def tags(self, tags: list[str]):
        """Set Device Tags"""
        update(self._api_client, self.serial_number, tags=tags)
        dataclasses.replace(self, _tags=tags)

    def add_tag(self, tag: str):
        """Add Device Tag"""
        tags = self.tags.copy()
        tags.append(tag)
        update(self._api_client, self.serial_number, tags=tags)
        dataclasses.replace(self, _tags=tags)

    def remove_tag(self, tag: str):
        """Remove Device Tag"""
        tags = self.tags.copy()
        tags.remove(tag)
        update(self._api_client, self.serial_number, tags=tags)
        dataclasses.replace(self, _tags=tags)

    def clear_tags(self):
        """Clear Device Tags"""
        tags: list[str] = []
        update(self._api_client, self.serial_number, tags=tags)
        dataclasses.replace(self, _tags=tags)

    def wipe(self):
        """Wipe Device"""
        bulk_operation(
            self._api_client, Operation.WIPE, device_udids=[self.device_uuid]
        )

    def restart(self):
        """Restart Device"""
        bulk_operation(
            self._api_client, Operation.RESTART, device_udids=[self.device_uuid]
        )

    def shutdown(self):
        """Shutdown Device"""
        bulk_operation(
            self._api_client, Operation.SHUTDOWN, device_udids=[self.device_uuid]
        )

    def clear_commands(self):
        """Clear Device Commands"""
        bulk_operation(
            self._api_client, Operation.CLEAR_COMMANDS, device_udids=[self.device_uuid]
        )

    def clear_failed_commands(self):
        """Clear Failed Device Commands"""
        bulk_operation(
            self._api_client,
            Operation.CLEAR_FAILED_COMMANDS,
            device_udids=[self.device_uuid],
        )

    def clear_pending_commands(self):
        """Clear Pending Device Commands"""
        bulk_operation(
            self._api_client,
            Operation.CLEAR_PENDING_COMMANDS,
            device_udids=[self.device_uuid],
        )

    def unassign(self):
        """Unassign Device from User / Send Device to Limbo"""
        bulk_operation(
            self._api_client, Operation.UNASSIGN, device_udids=[self.device_uuid]
        )

    def enable_lostmode(self):
        """Enable Lost Mode on Device"""
        lost_mode_operation(
            self._api_client, LostModeOperation.ENABLE, device_udids=[self.device_uuid]
        )

    def disable_lostmode(self):
        """Disable Lost Mode on Device"""
        lost_mode_operation(
            self._api_client, LostModeOperation.DISABLE, device_udids=[self.device_uuid]
        )

    def play_sound(self):
        """Play Lost Mode Sound on Device"""
        lost_mode_operation(
            self._api_client,
            LostModeOperation.PLAY_SOUND,
            device_udids=[self.device_uuid],
        )

    def request_location(self):
        """Request Lost Mode Location from Device"""
        lost_mode_operation(
            self._api_client,
            LostModeOperation.REQUEST_LOCATION,
            device_udids=[self.device_uuid],
        )


class DeviceCli:
    "Device CLI"

    @staticmethod
    @click.group(cls=OrderCommands)
    def device():
        """Device"""
        click.echo("Not implemented")
