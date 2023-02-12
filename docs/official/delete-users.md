
# Users Operations - Delete User

Key | Type | Required | Description
|-|-|-|-|
id | String max: 255 chars | Required | This is the User ID. This MUST be unique inside the School Database and will be used in other services.
operation | string | Required | delete

Example:

```php
$endpoint = '/users';
$parameters = array(
    'accessToken' => "YOUR-TOKEN",
    'elements' => array(
        array(
            'id' => 'user.staff.1',
            'operation' => 'delete', 
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
