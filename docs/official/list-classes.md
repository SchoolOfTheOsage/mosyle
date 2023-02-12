
# Classes - List Classes

Key | Type |  | Description
|-|-|-|-|
page | integer | Optional | The API will not send the entire list of classes in one request, rather it uses pagination (default: 1).
specific_columns | Array of strings | Optional | This option should be used to receive just the necessary attributes for each class. Possible values: id, class_name, course_name, location, teacher, students, coordinators, account.

Example:

```php
$endpoint = '/listclasses';
$parameters = array(
    'accessToken' => "YOUR-TOKEN",
    'options' => array(
        'specific_columns' => array('class_name', 'teacher', 'location')
    )
);
```

Success Response:

```json
{
  "status": "OK",
  "response": {
    "classes": [
      {
        "id": "dc093492-d2bf-4c0a-9a8e-5aadc541e250",
        "idclass": "123",
        "name": "Class I",
        "teacher": "john.smith",
        "locations": [
          "Townsville"
        ]
      }
  }
}
```

[Read Me](readme.md)
