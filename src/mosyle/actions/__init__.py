"""Mosyle Manager Python API - Action"""


class Action:
    """Action"""

    def get(
        self,
        page: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        id_users: list[str] | None = None,
    ):
        """Get Actions"""
        filter_options: dict[str, object] = {}
        if start_date is not None:
            filter_options["start_date"] = start_date
        if end_date is not None:
            filter_options["end_date"] = end_date
        if id_users is not None:
            filter_options["idusers"] = id_users

        keys: dict[str, object] = {}

        if page is not None:
            keys["page"] = page

        # return self.post(Endpoint.ACTIONS, keys=keys, filter_options=filter_options)
