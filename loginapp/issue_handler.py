
from ast import List
from flask import Blueprint, Response, jsonify, request

from loginapp.aspect import token_check
from loginapp.model.issue_req_model import IssueCreateRequest
from loginapp.model.issue_res_model import IssueListResponse
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
def all_issues_endpoint() -> Response:
    summary: str = request.args.get('summary', type = str)
    user_name: str = request.args.get('user_name', type = str)
    user_id: str = request.args.get('user_id', type = str)
    data: List[IssueListResponse] = issue_service.all_issues(summary, user_name, user_id, lambda x: IssueListResponse(
        x['issue_id'],
        x['summary'],
        x['created_at'],
        x['status'],
        x['user_id'],
        x['user_name'],
        x['profile_image'],
        x['comments']
    ))
    return jsonify({
        "data": data
    }), 200

@issue.get("/my")
@token_check(options = None)
def my_issues_endpoint() -> Response:
    summary: str = request.args.get('summary', type = str)
    user_id: int = SessionHolder.current_login().user_id
    data: List[IssueListResponse] = issue_service.all_issues(summary, None, user_id, lambda x: IssueListResponse(
        x['issue_id'],
        x['summary'],
        x['created_at'],
        x['status'],
        x['user_id'],
        x['user_name'],
        x['profile_image'],
        x['comments']
    ))
    return jsonify({
        "data": data
    }), 200
