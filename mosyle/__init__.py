from . import accounts, actions, cisco_ise, classes, devices, users

BASE_URL: str = "https://managerapi.mosyle.com/v2"
HEADERS = {
    "content-type": "application/json",
}
