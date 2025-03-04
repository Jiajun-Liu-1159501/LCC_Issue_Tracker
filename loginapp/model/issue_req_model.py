from dataclasses import dataclass
import re

from flask import Request

from loginapp.constant.issue_status import IssusStatus
from loginapp.constant.user_role import Role
from loginapp.exception.custom_error import ArgumentError


@dataclass
class IssueCreateRequest:

    summary: str
    description: str
    status: IssusStatus

    def build(request: Request) -> 'IssueCreateRequest':
        model: IssueCreateRequest =  IssueCreateRequest(
            request.form.get('summary'),
            request.form.get('description'),
            IssusStatus.NEW
        )
        model.verify()
        return model
    
    def verify(self) -> None:
        if not self.summary: raise ArgumentError("summary", "not a valid summary input")
        if not self.description: raise ArgumentError("description", "not a valid description input")


@dataclass
class AddCommentRequest:

    issue_id: int
    comment: str

    def build(request: Request) -> 'AddCommentRequest':
        model: AddCommentRequest =  AddCommentRequest(
            int(request.form.get('issue_id')),
            request.form.get('comment')
        )
        model.verify()
        return model
    
    def verify(self) -> None:
        if not self.comment: raise ArgumentError("comment", "not a valid comment input")
