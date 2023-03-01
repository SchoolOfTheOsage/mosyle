"""Mosyle Manager Python API - Device"""
from dataclasses import dataclass

from .api import Api


@dataclass(frozen=True, slots=True)
class Device:
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
    activation_bypass: str
    date_media_info: str
    tags: str
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
    asset_tag: str
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

    def get(self, serial_number: str):
        self = Api.list_devices(serial_numbers=serial_number)[0]

    def set_asset_tag(self, asset_tag: str):
        pass

    def set_name(self, name: str):
        pass

    def set_lock(self, lock: bool):
        pass

    def set_tags(self, tags: str):
        pass

    def add_tag(self, tag: str):
        pass

    def remove_tag(self, tag: str):
        pass

    def clear_tags(self):
        pass

    def wipe(self):
        pass

    def restart(self):
        pass

    def shutdown(self):
        pass

    def clear_commands(self):
        pass

    def clear_failed_commands(self):
        pass

    def clear_pending_commands(self):
        pass

    def unassign(self):
        pass

    def enable_lostmode(self):
        pass

    def disable_lostmode(self):
        pass

    def play_sound(self):
        pass

    def request_location(self):
        pass
