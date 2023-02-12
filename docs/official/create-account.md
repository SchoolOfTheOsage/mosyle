
# Accounts (District Only) -  Create new Account

Key | Type | Required | Description
|-|-|-|-|
operation | String | Required | The value of this operation must be 'request'.
school_name | String | Required | The name of the new account.
school_address | String | Required | The address info of the new account.
leader_name | String max: 100 chars | Optional | The name of the account leader.
leader_email | String max: 255 chars | Optional | The email of the account leader.
leader_id | String max: 255 chars | Optional | The id of the account leader.
uuid | String max: 255 chars | Optional

Example:

```php
$endpoint = '/accounts';
$parameters = array(
    'accessToken' => "YOUR-DISTRICT-TOKEN",
    'operation' => 'request',
    'school_name' => 'New School',
    'school_address' => 'New School Street',
    'leader_name' => 'New leader',
    'leader_email' => 'leader.email@example.com',
    'leader_id' => 'new.leader',
    'uuid' => '123123'
);
```

Success Response:

```json
{
  "status": "OK",
  "uuid": "123123"
}
```

[Read Me](readme.md)
