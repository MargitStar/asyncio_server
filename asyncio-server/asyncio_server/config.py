import json

from pydantic import BaseModel, Field
from json import JSONDecodeError


class ReadConfigError(Exception):
    pass


class AppConfig(BaseModel):
    host: str
    port: str


def read_config(path):
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except (JSONDecodeError, TypeError, OSError) as error:
        raise ReadConfigError(f'Cannot load config. error: {error}')
