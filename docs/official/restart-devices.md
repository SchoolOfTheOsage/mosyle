
# Devices Operations - Bulk Operations - Restart Devices

To restart a device you will pass the value bulkops through the endpoint and send the Unique Device Identifier through the key parameter devices or/and Device Groups ID through the key parameter groups. You can also send both commands at the same time.

Key | Type |  | Description
|-|-|-|-|
operation | String | Required | restart_devices
devices | Array | Required * | An array of Unique Device Identifier (UDID).
groups | Array | Optional | An array of Device Group IDs - Sends the command to all devices in the group

\* If any Device Group ID has been passed, it is not mandatory to inform the Unique Device Identifier.

Example:

```php
$endpoint = '/bulkops';

$parameters = array(
     'accessToken' => "YOUR-TOKEN",
     'elements' => array(
         array(
         'devices' => array('UDID1', 'UDID2'), 
         'operation' => 'restart_devices'
         )
     )
);
```

Success Response:

```json
{ 
    "status":"OK",
    "response":[ 
        { 
            "status":"COMMAND_SENT",
            "info":"Command sent successfully."
        }
    ]
}
```

[Read Me](readme.md)
