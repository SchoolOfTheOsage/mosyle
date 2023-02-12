
# Dynamic Device Groups Operations - List Devices

You will hit the endpoint /listdevicesbygroup and can send group ID to filter your request for the specific dynamic device group you want to receive in your response.

Available options:

Key | Type | Required | Description
|-|-|-|-|
iddevicegroup | string | Required | Dynamic Device Group ID (you can obtain this data using the "List Dynamic Device Groups" operation)

Your code will look like:

```php
$endpoint = '/listdevicesbygroup';
$parameters = [
   'accessToken' => 'YOUR-TOKEN',
   'options' => array(
     'iddevicegroup' => '123',
  )
];
```

Response:

```json
{
  status: "OK",
  response: {
      "group_name": "Class 101",
      "udids": [
        "1CD85FCF-04EA-5540-9E73-94FB4D36A392",
        "22473995-BE4A-0CE0-FA60-26827D981212",
        "E4ED28D6-6C5D-5B5C-93FB-AESAD12321J3"
      ]
  }
}
```

[Read Me](readme.md)
