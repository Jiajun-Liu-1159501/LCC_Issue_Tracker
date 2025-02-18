from abc import ABC
from datetime import datetime
from typing import TypeVar, Generic, Dict, Any
from dataclasses import dataclass

UE = TypeVar('User')

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
    def of(dict: Dict[str, Any]) -> UE:
        return User(
            dict.get('user_id'),
            dict.get('user_name'),
            dict.get('password'),
            dict.get('email'),
            dict.get('first_name'),
            dict.get('last_name'),
            dict.get('location'),
            dict.get('profile_image'),
            dict.get('role'),
            dict.get('status')
        )

IE = TypeVar('Issue')

@dataclass
class Issue:

    issue_id: int
    user_id: int
    summary: str
    descreption: str
    created_at: datetime
    status: str

    @staticmethod
    def of(dict: Dict[str, Any]) -> IE:
        return User(
            dict.get('issue_id'),
            dict.get('user_id'),
            dict.get('summary'),
            dict.get('descreption'),
            dict.get('created_at'),
            dict.get('status')
        )
    

CE = TypeVar('Comment')

@dataclass
class Comment:

    comment_id: int
    user_id: int
    issue_id: str
    content: str
    created_at: datetime

    @staticmethod
    def of(dict: Dict[str, Any]) -> CE:
        return User(
            dict.get('comment_id'),
            dict.get('user_id'),
            dict.get('issue_id'),
            dict.get('content'),
            dict.get('created_at')
        )