import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Env:
    def __init__(self, env):
        self.env = env

    def get_user_id(self):
        return os.environ.get("USER_ID") if self == "id" else None

    @staticmethod
    def get_email():
        return os.environ.get("EMAIL")

    @staticmethod
    def get_first_name():
        return os.environ.get("FIRST_NAME")

    @staticmethod
    def get_last_name():
        return os.environ.get("LAST_NAME")

    @staticmethod
    def get_avatar():
        return os.environ.get("AVATAR")
