from enum import Enum
from typing import TypeVar

US = TypeVar('UserStatus')

class UserStatus(Enum):

    ACTIVE = ("active")
    INACTIVE = ("inactive")

    def __new__(cls, value: str):
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    @classmethod
    def of(cls, name: str) -> US:
        return cls.__members__.get(name.upper(), None)