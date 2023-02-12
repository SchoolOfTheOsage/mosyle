
# Devices Operations - Lost Mode (iOS Only)

You will hit the endpoint /lostmode and send parameters to enable/disable lost mode and additional functions.

Key | Type |  | Description
|-|-|-|-|
operation | String | Required | enable</br>disable</br>play_sound</br>request_location
devices | Array of strings | Required * | Array of Unique Device Identifier (Device UDID)
groups | Array of strings | Optional | Array of Device Group ID
message | String | Required | Message to be shown on the screen
phone_number | String | Optional |  The phone number will be shown on the screen along with the message.  |
footnote | String | Optional | Footnote text will be shown on the screen along with the message.

\* If any Device Group ID has been passed, it is not mandatory to inform the Unique Device Identifier.

Example:

```php
$endpoint = '/lostmode';

$parameters = array(
     'accessToken' => "YOUR-TOKEN",
     'elements' => array(
         array(
         'devices' => array('UDID1', 'UDID2'),
         'operation' => 'enable',
         'message' => 'Lost Device',
         'footnote' => 'Additional footnote text'

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
