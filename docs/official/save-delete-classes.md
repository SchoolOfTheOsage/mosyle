
# Classes - Save and Delete Classes

Key | Type |  | Description
|-|-|-|-|
id | String (max: 100) | Required | Class ID in the Education Institution Database.
operation | String | Required | save: Save or update the class in the system.</br>delete: Delete the class
course_name | String max: 50 chars | Required | Course Name
class_name | String max: 50 chars | Required | Class Name
location | String max: 50 chars | Required | Location name. If the Location does not exist, one will be created with this name.
idteacher | String | Required | Teacher ID, same ID value entered in the User Web Service.
students | Array | Optional | Array of student IDs. The Student must be the same modality of the class. Class 1:1 just contain students 1:1.
room | String max: 50 chars | Optional | Room where the class is offered.
coordinators | Array | Optional | Array of Instructor User IDs. The User ID can not belong to a student.
platform | String | Optional | The absence of this value will default to the "ios" platform. This value can be ios or mac.

Example:

```php
$endpoint = '/classes';
$parameters = array(
    'accessToken' => "YOUR-TOKEN",
    'elements' =>  array(
        array(
            'operation' => 'save', 
            'id' => 'my.id', 
            'course_name' => 'ClassTestAPI',
            'class_name' => 'ClassTestAPI',
            'location' => 'TestAPILocation',
            'idteacher' => 'teacher.id'
        )
    )
);
```

Success Response:

```json
{
  "status": "OK",
  "uuid": "123456789"
}
```

[Read Me](readme.md)
