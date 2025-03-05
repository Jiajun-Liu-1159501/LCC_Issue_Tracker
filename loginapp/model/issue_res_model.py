from dataclasses import dataclass
import datetime
from typing import List


@dataclass
class IssueListResponse:
    """
    Represents a response containing a list of issues.

    Attributes:
        issue_id (int): The unique identifier for the issue.
        summary (str): A brief title or summary of the issue.
        created_at (datetime): The timestamp when the issue was created.
        issue_status (str): The current status of the issue (e.g., 'open', 'closed').
        user_id (int): The ID of the user who created the issue.
        user_name (str): The name of the user who created the issue.
        user_profile (str): A URL or path to the profile picture of the user who created the issue.
        comments (int): The number of comments associated with the issue.
    """
    
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
    """
    Represents a comment associated with an issue.

    Attributes:
        comment_id (int): The unique identifier for the comment.
        content (str): The text content of the comment.
        created_at (datetime): The timestamp when the comment was created.
        user_id (int): The ID of the user who wrote the comment.
        user_name (str): The name of the user who wrote the comment.
        user_profile (str): A URL or path to the profile picture of the user who wrote the comment.
        user_role (str): The role of the user who wrote the comment (e.g., 'admin', 'user').
    """
    
    comment_id: int
    content: str
    created_at: datetime
    user_id: int
    user_name: str
    user_profile: str
    user_role: str


@dataclass
class IssueDetailResponse:
    """
    Represents the detailed response for a specific issue.

    Attributes:
        issue_id (int): The unique identifier for the issue.
        summary (str): A brief title or summary of the issue.
        description (str): A detailed explanation of the issue.
        created_at (datetime): The timestamp when the issue was created.
        issue_status (str): The current status of the issue (e.g., 'open', 'closed').
        user_id (int): The ID of the user who created the issue.
        user_name (str): The name of the user who created the issue.
        user_profile (str): A URL or path to the profile picture of the user who created the issue.
        commentList (List[IssueComment]): A list of comments associated with the issue.
    """
    
    issue_id: int
    summary: str
    description: str
    created_at: datetime
    issue_status: str
    user_id: int
    user_name: str
    user_profile: str
    commentList: List[IssueComment]


