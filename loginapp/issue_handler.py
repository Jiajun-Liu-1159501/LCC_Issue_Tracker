
from typing import List
from flask import Blueprint, Response, jsonify, request

from loginapp.aspect import token_check
from loginapp.constant.user_role import Role
from loginapp.model.issue_req_model import AddCommentRequest, IssueCreateRequest
from loginapp.model.issue_res_model import IssueComment, IssueDetailResponse, IssueListResponse
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
@token_check(options = [Role.ADMIN, Role.HELPER])
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

@issue.get("/detail")
@token_check(options = None)
def issue_detail_endpoint() -> Response:
    issue_id: int = request.args.get('issue_id', type = int)
    data: IssueDetailResponse = issue_service.issue_detail(issue_id, lambda x, y: IssueDetailResponse(
        x['issue_id'],
        x['summary'],
        x['description'],
        x['created_at'],
        x['status'],
        x['user_id'],
        x['user_name'],
        x['profile_image'],
        list(map(lambda z: IssueComment(
            z['comment_id'],
            z['content'],
            z['created_at'],
            z['user_id'],
            z['user_name'],
            z['profile_image'],
            z['role'],
        ), y))
    ))
    return jsonify({
        "data": data
    }), 200

@issue.post("/comment")
@token_check(options = None)
def add_comment_endpoint() -> Response:
    req: AddCommentRequest = AddCommentRequest.build(request)
    user_id = SessionHolder.current_login().user_id
    issue_service.add_comment(user_id, req)
    return jsonify({
        "message": "success"
    }), 200
