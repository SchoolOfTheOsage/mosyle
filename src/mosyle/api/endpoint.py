"""Mosyle Manager Python API - API - Endpoint"""
"""Mosyle Manager Python API - API - Endpoint"""

from abc import ABC, abstractmethod, abstractproperty


class Endpoint(ABC):
    # ACTIONS = "actions"
    # LIST_DEVICES_BY_GROUP = "listdevicesbygroup"
    # LIST_DEVICE_GROUPS = "listdevicegroups"
    # GET_CISCO_ISE = "getciscoise"
    # CISCO_ISE = "ciscoise"
    # ACCOUNTS = "accounts"
    # LIST_CLASSES = "listclasses"
    # CLASSES = "classes"
    # USERS = "users"
    # LIST_USERS = "listusers"
    # LOST_MODE = "lostmode"
    # BULK_OPERATIONS = "bulkops"
    # DEVICES = "devices"
    # LIST_DEVICES = "listdevices"

    @property
    @abstractmethod
    def Endpoint(self):
        pass
