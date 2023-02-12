
# Device Operations - Update Device Attributes

| Key | Type | Required | Description
|-|-|-|-|
| serialnumber | String | Required | Serial number of the device that will be updated.
| asset_tag | String | Optional | To update the device asset tag.
| tags | String | Optional | To update the device tags. Multiple tags should be comma-separated.
| name | String | Optional | To update the device name.
| lock | String | Optional | To update the device lock message.

Example:

```php
$endpoint = '/devices';
$parameters = array(
    'accessToken' => "YOUR-TOKEN",
    'elements' =>  array(
        array(
            'serialnumber'=> 'AAAAAAAAAAAA',
            'name'        => 'New name',
            'tags'        => 'tag1, tag2',
        )
    )
);
```

Success Response:

```json
{
  "status": "OK",
  "devices": [
    "AAAAAAAAAAAA"
  ]
}
```

[Read Me](readme.md)
