
# Users Operations - Create/Update Users

To create a user you will pass the value save through the parameter operation.

Key | Type | Required | Description
|-|-|-|-|
id | String max: 255 chars | Required | This is the User ID. This MUST be unique inside the School Database and will be used for other services.
operation | string | Required | save
name | String max: 100 chars | Required | User Name
type | string | Required | Possible values:</br>S: Student</br>T: Teacher</br>STAFF: Staff
email | String max: 255 chars | Required (Optional for students and staff) | User E-mail address
managed_appleid | String max: 255 chars | Optional | Managed Apple ID created in ASM
locations | Array | Required for Students, Teachers, and Staff | Each array position should contain 2 keys: name, grade_level. The key 'grade_level' is required only for students (for other user types this key can be omitted). Location Name and Grade Level have a limit of 50 characters each.
welcome_email | Integer | Required Values: 1 (one); 0 (zero) | When the value is 1, Mosyle Manager will send an email with the instructions to login. This option will only work when the email field is not blank.

Example:

```php
$endpoint = '/users';
$parameters = array(
    'accessToken' => 'YOUR-TOKEN',
    'elements' => array(
        array(
            'id' => 'user.staff.1',
            'operation' => 'save', 
            'name' => 'User Staff 1',
            'type' => 'STAFF',
            'welcome_email' => 0,
            'email' => 'user.staff.1@example.mosyle.com',
            'locations' => array(array('name' => 'College (Mosyle)'))
        )
    )
);
```

Success Response:

```json
{
  'status': 'OK',
  'elements': [
    {
      'id': 'user.staff.1',
      'status': 'OK'
    }
  ]
}
```

[Read Me](readme.md)
