from datetime import datetime
from typing import TypeVar, List, Dict, Any
from dataclasses import dataclass

from loginapp.constant.issue_status import IssusStatus
from loginapp.constant.user_role import Role
from loginapp.constant.user_status import UserStatus

@dataclass
class User:

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
        return list(map(lambda x: User.of(x), data_list))
    
    def get_role_enum(self) -> Role:
        return Role.of(self.role)
    
    def get_status_enum(self) -> UserStatus:
        return UserStatus.of(self.status)
    

@dataclass
class Issue:

    issue_id: int
    user_id: int
    summary: str
    descreption: str
    created_at: datetime
    status: str

    @staticmethod
    def of(dict: Dict[str, Any]) -> 'Issue':
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
        return IssusStatus.of(self.status)


@dataclass
class Comment:

    comment_id: int
    user_id: int
    issue_id: str
    content: str
    created_at: datetime

    @staticmethod
    def of(dict: Dict[str, Any]) -> 'Comment':
        if dict == None or len(dict) == 0:
            return None
        return User(
            dict.get('comment_id'),
            dict.get('user_id'),
            dict.get('issue_id'),
            dict.get('content'),
            dict.get('created_at')
        )