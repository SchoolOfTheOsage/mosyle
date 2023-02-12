
# Devices Operations - List Devices

You will hit the endpoint /listdevices and can send parameters to filter your request for the specific info you want to receive in your response.

| Key | Type | Required | Description
|-|-------------|---|----------|
| os | String | Required | Which Operational System will be listed, values can be ios, mac, or tvos
| tags | Array of strings| Optional |
| osversions | Array of strings | Optional | |
| serial_numbers | Array of strings | Optional | Serial Numbers (filter by specific serial numbers)
| page| Integer | Optional | Pagination start with 0 |
| specific_columns | Array of strings | Optional | This option should be used to receive just the necessary attributes for each device. Possible values: deviceudid, total_disk, os, serial_number, device_name, device_model, battery, osversion, date_info, carrier, roaming_enabled, isroaming, imei, meid, available_disk, wifi_mac_address, last_ip_beat, last_lan_ip, bluetooth_mac_address, is_supervised, date_app_info, date_last_beat, date_last_push, status, isActivationLockEnabled, isDeviceLocatorServiceEnabled, isDoNotDisturbInEffect, isCloudBackupEnabled, IsNetworkTethered, needosupdate, productkeyupdate, device_type, lostmode_status, is_muted, date_muted, activation_bypass, date_media_info, tags, iTunesStoreAccountHash, iTunesStoreAccountIsActive, date_profiles_info, ethernet_mac_address, model_name, LastCloudBackupDate, SystemIntegrityProtectionEnabled, BuildVersion, LocalHostName, HostName, OSUpdateSettings, ActiveManagedUsers, CurrentConsoleManagedUser, date_printers, AutoSetupAdminAccounts, appleTVid, asset_tag, ManagementStatus, OSUpdateStatus, AvailableOSUpdates, appleTVid, enrollment_type, userid, username, usertype, SharedCartName, device_model_name, date_kinfo, location, latitude & longitude (only available for devices in lost mode) |

Example:

```php
$endpoint = '/listdevices';
$parameters = array(
    'accessToken' => "YOUR-TOKEN",
    'options' => array(
        'os' => 'ios'
    )
);
```

Success Response:

```json
{
  "status": "OK",
  "response": {
    "devices": [
      {
        "deviceudid": "001DFCEB-B160-5F2C-B435-2D4D9F4570E0",
        "total_disk": "256.0000000000",
        "os": "mac"
        ... others attributes and other devices
      }
    ],
    "rows": 1328,
    "page_size": 100,
    "page": 1
  }
}
```

[Read Me](readme.md)
