from dataclasses import dataclass
import datetime


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
