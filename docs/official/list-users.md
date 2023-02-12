
# Users Operations - List Users

Key | Type |  | Description
|-|-|-|-|
page | integer | Optional | The api does not send the entire list of users in one request, it needs to use pagination (default: 1).
specific_columns | Array of strings | Optional | This option should be used to receive just the necessary attributes for each user. Possible values: id, name, email, managedappleid, serial_number, type, locations, account.
types | Array of string | Optional | Filter users by type. Possible values: STUDENT, TEACHER, LOCATION_LEADER, STAFF, ADMIN, ACCOUNT_ADMIN, DISTRICT_ADMIN.

Example:

```php
$endpoint = '/listusers';
$parameters = array(
    'accessToken' => "YOUR-TOKEN",
    'options' => array(
        'specific_columns' => array('name', 'email', 'managedappleid', 'type', 'locations')
    )
);
```

Success Response:

```json
{
  "status": "OK",
  "response": {
    "users": [
      {
        "id": "dc093492-d2bf-4c0a-9a8e-5aadc541e250",
        "idusermosyle": "143",
        "name": "John Smith",
        "email": "john.smith@example.mosyle.com",
        "type": "STUDENT",
        "locations": [
          "Townsville"
        ]
      }
  }
}
```

[Read Me](readme.md)
