
from flask import Blueprint, request

from loginapp.aspect import token_check
from loginapp.model.issue_req_model import IssueCreateRequest
from loginapp.services import issue_service
from loginapp.session_holder import SessionHolder

issue: Blueprint = Blueprint('issue', __name__)

@issue.post("/create")
@token_check
def create_issue_endpoint() -> str:
    req: IssueCreateRequest = IssueCreateRequest.build(request)
    issue_service.create_issue(req, SessionHolder.current_login().user_id)
    return "success"

@issue.get("list")
def list_issue_endpoint() -> str:
    pass