
from flask import Blueprint, request

from loginapp.aspect import token_check
from loginapp.model.issue_req_model import IssueCreateRequest

issue: Blueprint = Blueprint('issue', __name__)

@issue.post("/create")
@token_check
def create_issue_endpoint() -> str:
    req: IssueCreateRequest = IssueCreateRequest.build(request)
