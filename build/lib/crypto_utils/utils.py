import os


def is_development() -> bool:
    if os.getenv("APP_ENV") != "prod":
        return True
    return False
