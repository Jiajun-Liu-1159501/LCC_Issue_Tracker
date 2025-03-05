from datetime import datetime
from typing import TypeVar, List, Dict, Any
from dataclasses import dataclass

from loginapp.constant.issue_status import IssusStatus
from loginapp.constant.user_role import Role
from loginapp.constant.user_status import UserStatus

@dataclass
class User:
    """
    Represents a user in the system.

    Attributes:
        user_id (int): Unique identifier for the user.
        user_name (str): The username of the user.
        password (str): The hashed password of the user.
        email (str): The email address of the user.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        location (str): The location of the user.
        profile_image (str): URL or path to the user's profile image.
        role (str): The role assigned to the user (e.g., 'admin', 'user').
        status (str): The status of the user (e.g., 'active', 'inactive').

    Methods:
        of(dict: Dict[str, Any]) -> 'User':
            Converts a dictionary to a User object.
        
        of_all(data_list: List[Dict[str, Any]]) -> List['User']:
            Converts a list of dictionaries to a list of User objects.
        
        get_role_enum() -> Role:
            Returns the Role enum corresponding to the user's role.
        
        get_status_enum() -> UserStatus:
            Returns the UserStatus enum corresponding to the user's status.
    """

    user_id: int
    user_name: str
    password: str
    email: str
    first_name: str
    last_name: str
    location: str
    profile_image: str
    role: str
    status: str

    @staticmethod
    def of(dict: Dict[str, Any]) -> 'User':
        """
        Converts a dictionary into a User object.

        Args:
            dict (Dict[str, Any]): A dictionary containing the user data.

        Returns:
            User: A User object populated with the data from the dictionary.
        
        Note:
            If the dictionary is empty or None, it returns None.
        """
        if dict == None or len(dict) == 0:
            return None
        return User(
            dict.get('user_id'),
            dict.get('user_name'),
            dict.get('password_hash'),
            dict.get('email'),
            dict.get('first_name'),
            dict.get('last_name'),
            dict.get('location'),
            dict.get('profile_image'),
            dict.get('role'),
            dict.get('status')
        )
    
    @staticmethod
    def of_all(data_list: List[Dict[str, Any]]) -> List['User']:
        """
        Converts a list of dictionaries into a list of User objects.

        Args:
            data_list (List[Dict[str, Any]]): A list of dictionaries containing user data.

        Returns:
            List[User]: A list of User objects populated with the data from the dictionaries.
        """

        return list(map(lambda x: User.of(x), data_list))
    
    def get_role_enum(self) -> Role:
        """
        Converts the role string into a Role enum.

        Returns:
            Role: The corresponding Role enum for the user.
        """
        return Role.of(self.role)
    
    def get_status_enum(self) -> UserStatus:
        """
        Converts the status string into a UserStatus enum.

        Returns:
            UserStatus: The corresponding UserStatus enum for the user.
        """
        return UserStatus.of(self.status)
    

@dataclass
class Issue:
    """
    Represents an issue in the system.

    Attributes:
        issue_id (int): Unique identifier for the issue.
        user_id (int): The ID of the user who created the issue.
        summary (str): A brief summary of the issue.
        descreption (str): A detailed description of the issue.
        created_at (datetime): The timestamp when the issue was created.
        status (str): The status of the issue (e.g., 'open', 'closed').

    Methods:
        of(dict: Dict[str, Any]) -> 'Issue':
            Converts a dictionary to an Issue object.
        
        get_status_enum() -> IssusStatus:
            Returns the IssusStatus enum corresponding to the issue's status.
    """

    issue_id: int
    user_id: int
    summary: str
    descreption: str
    created_at: datetime
    status: str

    @staticmethod
    def of(dict: Dict[str, Any]) -> 'Issue':
        """
        Converts a dictionary into an Issue object.

        Args:
            dict (Dict[str, Any]): A dictionary containing the issue data.

        Returns:
            Issue: An Issue object populated with the data from the dictionary.
        
        Note:
            If the dictionary is empty or None, it returns None.
        """
        if dict == None or len(dict) == 0:
            return None
        return Issue(
            dict.get('issue_id'),
            dict.get('user_id'),
            dict.get('summary'),
            dict.get('descreption'),
            dict.get('created_at'),
            dict.get('status')
        )
    
    def get_status_enum(self) -> IssusStatus:
        """
        Converts the status string into an IssusStatus enum.

        Returns:
            IssusStatus: The corresponding IssusStatus enum for the issue.
        """
        return IssusStatus.of(self.status)


@dataclass
class Comment:
    """
    Represents a comment made by a user on an issue.

    Attributes:
        comment_id (int): Unique identifier for the comment.
        user_id (int): The ID of the user who made the comment.
        issue_id (str): The ID of the issue the comment is associated with.
        content (str): The text content of the comment.
        created_at (datetime): The timestamp when the comment was created.

    Methods:
        of(dict: Dict[str, Any]) -> 'Comment':
            Converts a dictionary to a Comment object.
    """

    comment_id: int
    user_id: int
    issue_id: str
    content: str
    created_at: datetime

    @staticmethod
    def of(dict: Dict[str, Any]) -> 'Comment':
        """
        Converts a dictionary into a Comment object.

        Args:
            dict (Dict[str, Any]): A dictionary containing the comment data.

        Returns:
            Comment: A Comment object populated with the data from the dictionary.
        
        Note:
            If the dictionary is empty or None, it returns None.
        """
        if dict == None or len(dict) == 0:
            return None
        return User(
            dict.get('comment_id'),
            dict.get('user_id'),
            dict.get('issue_id'),
            dict.get('content'),
            dict.get('created_at')
        )