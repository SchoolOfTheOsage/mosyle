"""Mosyle Manager Python API - Device"""
import dataclasses
from dataclasses import dataclass

from ..api import ApiClient
from .api import *
from .lostmode_operation import LostModeOperation
from .operation import Operation
from .platform import Platform


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
