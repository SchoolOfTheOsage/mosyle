import requests
from requests.auth import HTTPBasicAuth

from .defaults import REQUEST_HEADERS, REQUEST_TIMEOUT, REQUEST_URL


class DeviceOs:
    """Device Operating Systems"""

    MAC_OS = "mac"
    I_OS = "ios"
    TV_OS = "tvos"


class DeviceAttributes:
    """Device Attributes"""

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
    ACTIVATION_BYPASS = "activation_bypass"
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


class DeviceOperation:
    """Device Operations"""

    WIPE_DEVICES = "wipe_devices"
    RESTART_DEVICES = "restart_devices"
    SHUTDOWN_DEVICES = "shutdown_devices"
    CLEAR_COMMANDS = "clear_commands"
    CLEAR_PENDING_COMMANDS = "clear_pending_commands"
    CLEAR_FAILED_COMMANDS = "clear_failed_commands"
    CHANGE_TO_LIMBO = "change_to_limbo"


class DeviceLostModeOperation:
    """Device Lost Mode Operations"""

    ENABLE = "enable"
    DISABLE = "disable"
    PLAY_SOUND = "play_sound"
    REQUEST_LOCATION = "request_location"


DeviceGroupOs = DeviceOs


class Devices:
    def __init__(
        self,
        device_os: str,
        access_token: str,
        username: str | None = None,
        password: str | None = None,
    ):
        self.devices: list[dict[str, object]] = []
        self.device_os = device_os
        self.access_token = access_token
        if username is not None and password is not None:
            self.auth = HTTPBasicAuth(username, password)
        else:
            self.auth = None

    def read(
        self,
        devices_os: str,
        tags: list[str] | None = None,
        os_versions: list[str] | None = None,
        serial_numbers: list[str] | None = None,
        page: int | None = None,
        specific_columns: list[str] | None = None,
    ):
        url = f"{REQUEST_URL}/listdevices"

        options: dict[str, object] = {
            "os": devices_os,
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

        response = requests.post(
            url,
            json=payload,
            headers=REQUEST_HEADERS,
            timeout=REQUEST_TIMEOUT,
        ).json()

        self.devices = response["devices"]

    def _list_devices_by_group(
        self,
        device_group_id: str,
    ) -> dict[str, object]:
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

    def _list_device_groups(self, operating_system: str) -> dict[str, object]:
        url = f"{REQUEST_URL}/listdevicegroups"

        options = {
            "os": operating_system,
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

    def _update_device_attribute(
        self,
        serial_number: str,
        asset_tag: str | None = None,
        tags: str | None = None,
        name: str | None = None,
        lock: str | None = None,
    ):
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

    def _bulk_operations(
        self,
        operation: str,
        device_udids: list[str] | None = None,
        group_ids: list[str] | None = None,
        pin_code: str | None = None,
        preserve_data_plan: bool | None = None,
        disallow_proximity_setup: bool | None = None,
        revoke_vpp_license: bool | None = None,
    ) -> dict[str, object]:
        url = f"{REQUEST_URL}/bulkops"

        if device_udids is None and group_ids is None:
            device_udids = [
                str(devices[DeviceAttributes.DEVICE_UDID]) for devices in self.devices
            ]

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
        if len(options) > 0:
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

    def _lost_mode_operations(
        self,
        operation: str,
        device_udids: list[str] | None = None,
        group_ids: list[str] | None = None,
        message: str | None = None,
        phone_number: str | None = None,
        footnote: str | None = None,
    ):
        url = f"{REQUEST_URL}/lostmode"

        if device_udids is None and group_ids is None:
            device_udids = [
                str(devices[DeviceAttributes.DEVICE_UDID]) for devices in self.devices
            ]

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
