
# Action Logs - List

Key | Type |  | Description
|-|-|-|-|
page | Integer | Optional | The API does not send the entire list of logs in one request. Pagination should be used to get more data if the response has more pages (default: 1).
filter_options | Array of strings | Optional | Values that can be used to filter the Action Logs: start_date (timestamp), end_date (timestamp), idusers (array of users id).


Example:

```php
$endpoint = '/adminlogs';
 $parameters = [
   'accessToken' => 'YOUR-TOKEN',
   'page' => 1,
   'filter_options' => array(
     'start_date' => '1614556800',
     'end_date' => '1615939200',
     'idusers' => [000]
  )
 ];
```

Success Response:

```json
{
  "status": "OK",
  "response": [
    {
      "logs": [
        {
          "action": "Save Profile",
          "details": {
            "Profile Type": "Install App",
            "Operating System": "macOS",
          },
          "username": "Catalog",
          "action_date": "2021-03-01",
          "ip": "127.0.0.1"
        }
      ],
      "rows": "1",
      "page_size": 50,
      "page": 1
    }
  ]
}
```

[Read Me](readme.md)
