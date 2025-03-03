
from flask import Blueprint, Response, jsonify, request

from loginapp.aspect import token_check
from loginapp.model.issue_req_model import IssueCreateRequest
from loginapp.services import issue_service
from loginapp.session_holder import SessionHolder

issue: Blueprint = Blueprint('issue', __name__)

@issue.post("/create")
@token_check(options = None)
def create_issue_endpoint() -> Response:
    req: IssueCreateRequest = IssueCreateRequest.build(request)
    issue_service.create_issue(req, SessionHolder.current_login().user_id)
    return jsonify({
        "message": "success"
    }), 200

@issue.get("/all")
@token_check(options = None)
def all_issue_endpoint() -> str:
    summary: str = request.args.get('summary', type = str)
    user_name: str = request.args.get('user_name', type = str)
    user_id: str = request.args.get('user_id', type = str)
    issue_service.all_issues(summary, user_name, user_id, )
