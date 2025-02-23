from enum import Enum
from typing import List

class Role(Enum):

    ADMIN = ("admin", ["home", "my_issues", "all_issues", "user_management"])
    HELPER = ("helper", ["home", "my_issues", "all_issues"])
    VISITOR = ("visitor", ["home", "my_issues", "all_issues"])

    def __new__(cls, value: str, allowed_operations: List[str]):
        obj = object.__new__(cls)
        obj._value_ = value  
        obj._allowed_operations = allowed_operations
        return obj

    @classmethod
    def of(cls, name: str) -> 'Role':
        return cls.__members__.get(name.upper())
    
    def get_allowed_operations(self) -> List[str]: 
        return self._allowed_operations