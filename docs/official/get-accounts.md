
# Accounts (District Only) - Get Accounts

When in a district just hit the endpoint /accounts to get a list of all accounts.

Example:

```php
$endpoint = '/accounts';
$parameters = array(
    'accessToken' => "YOUR-TOKEN",
);
```

Success Response:

```json
{
  "status": "OK",
  "accounts": [
    {
      "idaccount": "1",
      "name": "Account 1",
      "address": "Street 1",
      "date_created": "1556195183"
    },
    {
      "idaccount": "2",
      "name": "Account 2",
      "address": "Street 2",
      "date_created": "1556195196"
    }
  ]
}
```

[Read Me](readme.md)
