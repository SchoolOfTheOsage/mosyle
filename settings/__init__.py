import json


class Settings:
    def __init__(self):
        self.settings: dict[str, str] = {}

    def load(self):
        with open("settings.json", "r", encoding="utf8") as file:
            self.settings = json.load(file)

    def commit(self):
        with open("settings.json", "w", encoding="utf8") as file:
            json.dump(self.settings, file)

    def create_key(self, key: str, value: str):
        self.settings[key] = value

    def read_key(self, key: str):
        return self.settings[key]

    def update_key(self, key: str, value: str):
        self.settings[key] = value

    def delete_key(self, key: str):
        del self.settings[key]
