from dataclasses import dataclass

from flask import Request

from loginapp.constant.issue_status import IssusStatus
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
        if not self.summary: raise ArgumentError("not a valid summary input")
        if not self.description: raise ArgumentError("not a valid description input")