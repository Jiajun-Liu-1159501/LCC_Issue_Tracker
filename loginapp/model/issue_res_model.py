from dataclasses import dataclass
import datetime
from typing import List


@dataclass
class IssueListResponse:
    
    issue_id: int
    summary: str
    created_at: datetime
    issue_status: str
    user_id: int
    user_name: str
    user_profile: str
    comments: int


@dataclass
class IssueComment:
    
    comment_id: int
    content: str
    created_at: datetime
    user_id: int
    user_name: str
    user_profile: str
    user_role: str


@dataclass
class IssueDetailResponse:
    
    issue_id: int
    summary: str
    description: str
    created_at: datetime
    issue_status: str
    user_id: int
    user_name: str
    user_profile: str
    commentList: List[IssueComment]


