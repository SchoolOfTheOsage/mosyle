
# Cisco ISE - Add and Remove Devices

Key | Type | Required | Description
|-|-|-|-|
action | String | Required | Values can be add or remove, in order to add or remove the mac address and serial number from the Cisco ISE list.
wifimac | String | Required | 
serialnumber | String | Required | 
model | String | Optional | Device model, Limit 50 characters.

Example:

```php
$endpoint = '/ciscoise';
$parameters = array(
    'accessToken' => "YOUR-TOKEN",
    'elements' =>  array(
        array(
            'action' => 'add', 
            'wifimac' => "5C:96:9D:71:6E:17",
            'serialnumber' => 'C02JK;S9WDTY3'
        )
    )
);
```

[Read Me](readme.md)
