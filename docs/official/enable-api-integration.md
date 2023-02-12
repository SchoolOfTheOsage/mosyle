# How do I enable the API Integration?

The API Integration is available for all Mosyle Manager Premium accounts. You can access the API Integration by going to My School > Integrations > + Activate New Integration > API Integration.

API requests require Admin User Credentials for authorization. You can create an Admin user specifically for the API integration under My School > Users > Administrators and limit the user's permissions to only API access.

When making requests, please include the following Authorization information in the header:

`--header 'Authorization: Basic BASE_64_ENCODED_EMAIL_AND_PASSWORD'`

To obtain this base64 encoded value, you can run the following command in Terminal:

`echo -n 'EMAIL:PASSWORD' | openssl base64`

Note: Be sure to substitute the correct email address and password before running the command above

Last Update: 11/28/2022 02:49 PM

[Mosyle Article](https://myschool.mosyle.com/#helpcenter/1260)

[Read Me](readme.md)
