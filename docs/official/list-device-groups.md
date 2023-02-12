
# Dynamic Device Groups Operations - List Dynamic Device Groups

You will hit the endpoint /listdevicegroups and can send parameters to filter your request for the specific info you want to receive in your response or receive all info about dynamic device groups.

Available options:

Key | Type | Required | Description
|-|-|-|-|
os | enum ('ios', 'mac', 'tvos') | Required | Operational system
page | integer | Optional | Pagination starting with 0

Your code will looks like:

```php
$endpoint = '/listdevicegroups';
$parameters = [
      'accessToken' => 'YOUR-TOKEN',
      'options' => array(
            'os' => 'ios',
     )
];
```

Response:

```json
{
  status: "OK",
  response: [
    {
      groups: [
        {
          id: "210",
          name: "My Device Group",
          device_numbers: "3",
        }
      ],
      rows: 1
      page_size: 50
      page: 1
    }
  ]
}
```

Without 'os' key:

```json
{
  status: "OK",
  response: [
    {
      status: "MISSING_DATA",
      info: "Missing key: os"
    }
  ]
}
```

[Read Me](readme.md)
