class Classes:
    def __init__(self):
        self.classes = []


class ClassOperations:
    """Class Operations"""

    ENDPOINT = "/classes"


class ClassOperationTypes:
    """Class Operations"""

    SAVE = "save"
    DELETE = "delete"


class ClassPlatform:
    """Class Platforms"""

    IOS = "ios"
    MAC = "mac"


class ReadClasses:
    """Read Classes"""

    ENDPOINT = "/listclasses"


class ClassAttributes:
    """Class Attributes"""

    ID = "id"
    CLASS_NAME = "class_name"
    COURSE_NAME = "course_name"
    LOCATION = "location"
    TEACHER = "teacher"
    STUDENTS = "students"
    COORDINATORS = "coordinators"
    ACCOUNT = "account"
