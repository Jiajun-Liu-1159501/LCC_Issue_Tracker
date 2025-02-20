from enum import Enum
import re
from typing import List, TypeVar

R = TypeVar('Role')

class Role(Enum):

    ADMIN = ("admin", "111")
    HELPER = ("helper", "222")
    VISIOTR = ("helper", "333")

    def __new__(cls, value: str, home_page: str):
        obj = object.__new__(cls)
        obj._value_ = value  
        obj._home_page = home_page
        return obj

    @classmethod
    def of(cls, name: str) -> R:
        return cls.__members__.get(name.upper(), None)
    
    def get_home_page(self) -> str: 
        return self._home_page