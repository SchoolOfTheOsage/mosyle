"""Mosyle Manager Python API - Cisco ISE"""
from dataclasses import dataclass

from .api_client import ApiClient
from .str_enum import StrEnum


class CiscoIseApiResource(StrEnum):
    """Cisco ISE API Resource Enumeration"""

    GET = "getciscoise"
    OPERATION = "ciscoise"


class CiscoIseOperation(StrEnum):
    """Cisco Ise Operation Enumeration"""

    ADD = "add"
    REMOVE = "remove"


@dataclass(frozen=True, slots=True)
class CiscoIse:
    """Cisco ISE"""

    def get(self, paging: int):
        """Get Cisco ISE"""

        # keys = {
        #    "paging": paging,
        # }

        # return self.post(Endpoint.GET_CISCO_ISE, keys=keys)

    def operation(
        self,
        action: CiscoIseOperation,
        wifimac: str,
        serialnumber: str,
        model: str | None = None,
    ):
        """Cisco ISE Operation"""

        element: dict[str, object] = {
            "action": action,
            "wifimac": wifimac,
            "serialnumber": serialnumber,
        }

        if model is not None:
            element["model"] = model

        # return self.post(Endpoint.CISCO_ISE, elements=[element])
