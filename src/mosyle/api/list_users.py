from .endpoint import Endpoint


class ListUsers(Endpoint):
    ENDPOINT = "listusers"

    def __init__(self):
        self.Endpoint = "listusers"
