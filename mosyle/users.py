class Users:
    def __init__(self):
        self.users = []


class ReadUsers:
    """Read Users"""

    ENDPOINT = "/listusers"


class UserAttributes:
    """User Attributes"""

    ID = "id"
    NAME = "name"
    EMAIL = "email"
    MANAGED_APPLE_ID = "managedappleid"
    SERIAL_NUMBER = "serial_number"
    TYPE = "type"
    LOCATIONS = "locations"
    ACCOUNT = "account"


class ReadUserTypes:
    """User Types"""

    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    LOCATION_LEADER = "LOCATION_LEADER"
    STAFF = "STAFF"
    ADMIN = "ADMIN"
    ACCOUNT_ADMIN = "ACCOUNT_ADMIN"
    DISTRICT_ADMIN = "DISTRICT_ADMIN"


class UpdateUsers:
    """Update Users"""

    ENDPOINT = "/users"

    class Type:
        """User Types"""

        STUDENT = "S"
        TEACHER = "T"
        STAFF = "STAFF"
