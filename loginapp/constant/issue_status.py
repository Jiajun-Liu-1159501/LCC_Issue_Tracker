from enum import Enum
from typing import List, TypeVar

IS = TypeVar('IssusStatus')

class IssusStatus(Enum):

    NEW = ("new")
    OPEN = ("open")
    STALLED = ("stalled")
    CLOSED = ("closed")

    def __new__(cls, value: str):
        obj = object.__new__(cls)
        obj._value_ = value  
        return obj

    @classmethod
    def of(cls, name: str) -> R:
        return cls.__members__.get(name.upper(), None)