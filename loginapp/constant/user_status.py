from enum import Enum
from typing import TypeVar

US = TypeVar('UserStatus')

class UserStatus(Enum):
    """
    Enum representing the status of a user (ACTIVE, INACTIVE).
    """

    ACTIVE = ("active")
    INACTIVE = ("inactive")

    def __new__(cls, value: str):
        """
        Custom constructor for UserStatus enum to associate the status with its value.

        Args:
            cls (type): The enum class.
            value (str): The status value (active or inactive).
        """
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    @classmethod
    def of(cls, name: str) -> US:
        """
        Returns the UserStatus corresponding to the provided name.

        Args:
            name (str): The status name (e.g., "ACTIVE", "INACTIVE").

        Returns:
            UserStatus: The corresponding UserStatus enum.
        """
        return cls.__members__.get(name.upper(), None)