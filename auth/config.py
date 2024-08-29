import os

class Config:
    SECRET_KEY = "8f3a12b9e7c54d6a9f0d2e1c8b7a3f6e"
    DATABASE_URL = "sqlite:///./test.db"
    PASSWORD_SALT = "e9f8d7c6b5a4321098765432109876fe"
    TOKEN_EXPIRATION = 3600

    @staticmethod
    def load_config():
        return Config()

config = Config.load_config()