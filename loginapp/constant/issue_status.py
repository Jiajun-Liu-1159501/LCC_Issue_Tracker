from enum import Enum
from typing import List, TypeVar

IS = TypeVar('IssusStatus')

class IssusStatus(Enum):
    """
    Enum representing different issue statuses.
    """

    NEW = ("new")
    OPEN = ("open")
    STALLED = ("stalled")
    RESOLVED = ("resolved")

    def __new__(cls, value: str):
        """
        Custom __new__ method to set the value for each status.

        Args:
            cls (type): The enum class.
            value (str): The string value of the status.

        Returns:
            IssueStatus: The created enum instance.
        """
        obj = object.__new__(cls)
        obj._value_ = value  
        return obj

    @classmethod
    def of(cls, name: str) -> IS:
        """
        Returns the IssueStatus corresponding to the provided name.

        Args:
            name (str): The name of the status.

        Returns:
            IssueStatus: The corresponding IssueStatus or None if not found.
        """
        return cls.__members__.get(name.upper(), None)