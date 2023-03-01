"""Mosyle Manager Python API - Account"""
from dataclasses import dataclass

from .api_client import ApiClient
from .str_enum import StrEnum


class AccountApiResource(StrEnum):
    """Account API Resource Enumeration"""

    OPERATION = "accounts"


class AccountOperation(StrEnum):
    """Account Operation Enumeration"""

    LIST = None
    REQUEST = "request"


@dataclass(frozen=True, slots=True)
class Account:
    """Account"""

    def operation(
        self,
        operation: AccountOperation | None = None,
        school_name: str | None = None,
        school_address: str | None = None,
        leader_name: str | None = None,
        leader_email: str | None = None,
        leader_id: str | None = None,
        uuid: str | None = None,
    ):
        """Account Operations"""

        keys = {}
        if operation is not None:
            keys["operation"] = operation
        if school_name is not None:
            keys["school_name"] = school_name
        if school_address is not None:
            keys["school_address"] = school_address
        if leader_name is not None:
            keys["leader_name"] = leader_name
        if leader_email is not None:
            keys["leader_email"] = leader_email
        if leader_id is not None:
            keys["leader_id"] = leader_id
        if uuid is not None:
            keys["uuid"] = uuid

        # return self.post(Endpoint.ACCOUNTS, keys=keys)
