
# Device Operations - Bulk Operations - Clear Commands

To clear commands you will pass the value bulkops through the endpoint and send the Unique Device Identifier through the key parameter devices or/and Device Groups ID through the key parameter groups. You can also send both commands at the same time.

Key | Type | Required | Description
|-|-|-|-|
operation | String | Required | clear_commands (pending + failed)</br>clear_pending_commands</br>clear_failed_commands
devices | Array | Required * | An array of Unique Device Identifier (UDID).
groups | Array | Optional | An array of Device Group IDs - Sends the command to all devices in the group

/* If any Device Group ID has been passed, it is not mandatory to inform the Unique Device Identifier.

Example:

```php
$endpoint = '/bulkops';

$parameters = array(
     'accessToken' => "YOUR-TOKEN",
     'elements' => array(
         array(
             'devices' => array('UDID1', 'UDID2'), 
             'operation' => 'clear_commands',
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
         "status":"COMMAND_CLEARED",
         "info":"Command cleared successfully."
       }
   ]
}
```

[Read Me](readme.md)
