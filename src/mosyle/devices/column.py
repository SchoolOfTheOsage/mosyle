from ..str_enum import StrEnum


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
