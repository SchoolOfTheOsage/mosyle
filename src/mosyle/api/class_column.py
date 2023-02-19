"""Mosyle Class Column Enumerations"""
from enum import Enum


class ClassColumn(str, Enum):
    """Mosyle Class Column Enumerations"""

    ID = "id"
    CLASS_NAME = "class_name"
    COURSE_NAME = "course_name"
    LOCATION = "location"
    TEACHER = "teacher"
    STUDENTS = "students"
    COORDINATORS = "coordinators"
    ACCOUNT = "account"

    def __str__(self) -> str:
        return str.__str__(self)
