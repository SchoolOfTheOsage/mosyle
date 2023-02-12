
# Users Operations - Assign Devices

Key | Type | Required | Description
|-|-|-|-|
id | String max: 255 chars | Required | This is the User ID. This MUST be unique inside the School Database and will be used for other services.
operation | string | Required | assign_device
serial_number | string | Required | Assign a specific device to the user.

Example:

```php
$endpoint = '/users';
$parameters = array(
    'accessToken' => "YOUR-TOKEN",
    'elements' => array(
        array(
            'id' => 'user.staff.1',
            'operation' => 'assign_device', 
            'serial_number' => 'AAAAAAAAAAAA',
        )
    )
);
```

Success Response:

```json
{
  "status": "OK",
  "elements": [
    {
      "id": "user.staff.1",
      "status": "OK"
    }
  ]
}
```

[Read Me](readme.md)
