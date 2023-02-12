# First Steps - How to make a Request using the API

To use the Mosyle API you need to enable this feature in the API profile page (My School > API Integration > Enable the profile).

Once enabled you will be able to see your access token and make requests to the endpoint "https://managerapi.mosyle.com/v2", every request will have some required parameters as well as optional parameters. You can send these parameters as key => value using the form-data format or a JSON format. Check the list below with the required parameters:

| Key | Type | Required | Description
|-|-|-|-|
| accessToken | string | Required | Mosyle API access key.
| Authorization | string | Required | The string 'Basic' followed by the base64 encoded 'username:password'
| idaccount or uuid | string | Required | if District Level School ID Account or UUID for the school. |

The following code snippet is generic enough to be used in all of your API requests. The only things that can change are the variables $endpoint and $parameters['elements']. For more examples with other languages and to test the API, [click here to download the API sample file](https://myschool.mosyle.com/downloads/api-docs/API%20Manager.json). (Compatible with Postman and Insomnia).

Attention: You must change the environment variables, provide your API Access Token, as well as Authorization credentials when you open the sample archive on Postman or Insomnia.

```php
<?php

$endpoint = '/listusers';


$username = 'email that will be authenticated in Mosyle Manager';
$password = '**************************************';


$parameters = array(
 'accessToken' => 'your API access token',
 // Additional parameters, eg.:
 // 'options' => array(),
);

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, 'https://managerapi.mosyle.com/v2' . $endpoint); // start the curl

curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); // return the transfer as a string


curl_setopt($ch, CURLOPT_POST, true); // set as post request


curl_setopt($ch, CURLOPT_HTTPHEADER, array('Authorization: Basic '.base64_encode($username.':'.$password)));

curl_setopt($ch, CURLOPT_POSTFIELDS, array('content' => json_encode($parameters)));




$output = curl_exec($ch); // $output contains the output string


// close curl resource to free up system resources

curl_close($ch);
echo $output;
```


Check the next articles to learn more about the services and their operations.

[Read Me](readme.md)
