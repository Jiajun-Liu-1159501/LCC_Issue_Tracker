from enum import Enum
from typing import List

class Role(Enum):
    """
    Enum representing different user roles and their allowed operations.
    """

    ADMIN = ("admin", ["home", "my_issues", "all_issues", "user_management"])
    HELPER = ("helper", ["home", "my_issues", "all_issues"])
    VISITOR = ("visitor", ["home", "my_issues"])

    def __new__(cls, value: str, allowed_operations: List[str]):
        """
        Custom constructor for Role enum to associate roles with allowed operations.

        Args:
            cls (type): The enum class.
            value (str): The role value (admin, helper, visitor).
            allowed_operations (List[str]): List of allowed operations for the role.
        """
        obj = object.__new__(cls)
        obj._value_ = value  
        obj._allowed_operations = allowed_operations
        return obj

    @classmethod
    def of(cls, name: str) -> 'Role':
        """
        Returns the Role corresponding to the provided name.

        Args:
            name (str): The role name (e.g., "ADMIN", "HELPER").

        Returns:
            Role: The corresponding Role enum or None if not found.
        """
        return cls.__members__.get(name.upper())
    
    def get_allowed_operations(self) -> List[str]:
        """
        Returns the list of allowed operations for the role.

        Returns:
            List[str]: The allowed operations for the role.
        """ 
        return self._allowed_operations