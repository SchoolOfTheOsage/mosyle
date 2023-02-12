
# Device Operations - Bulk Operations - Wipe Devices

To wipe a device you will pass the value bulkops through the endpoint and send the Unique Device Identifier through the key parameter devices or/and Device Groups ID through the key parameter groups. You can also send both commands at the same time.

|Key | Type |  | Description|
|-|-|-|-|
|operation | String | Required | wipe_devices|
|devices | Array | Required* | An array of Unique Device Identifier (UDID).|
|groups | Array | Optional | An array of Device Group IDs - Sends the command to all devices in the group|
|options | Object (key => value) | Optional | pin_code (6 digits) [macOS only] </br> PreserveDataPlan (bool) [iOS only]</br>DisallowProximitySetup (bool) [iOS only]</br>RevokeVPPLicenses (bool) [iOS & tvOS only]|

\* If any Device Group ID has been passed, it is not mandatory to inform the Unique Device Identifier.

Example:

```php
$endpoint = '/bulkops';

$parameters = array(
     'accessToken' => "YOUR-TOKEN",
     'elements' => array(
         array(
             'devices' => array('UDID1', 'UDID2'), 
             'operation' => 'wipe_devices',
             'options' => array(
             'pin_code' => '123456',
             'PreserveDataPlan' => false,
             'DisallowProximitySetup' => false,
             'RevokeVPPLicenses' => false
         )
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
