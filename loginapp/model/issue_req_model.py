from dataclasses import dataclass

from flask import Request

from loginapp.constant.issue_status import IssusStatus
from loginapp.constant.user_role import Role
from loginapp.exception.custom_error import ArgumentError


@dataclass
class IssueCreateRequest:
    """
    Represents a request to create an issue.

    Attributes:
        summary (str): A brief title or description of the issue.
        description (str): A detailed explanation of the issue.
        status (IssusStatus): The status of the issue (default is 'NEW').

    Methods:
        build(request: Request) -> 'IssueCreateRequest':
            Builds an IssueCreateRequest instance from a Flask request.
        
        verify() -> None:
            Validates the required fields for the issue creation request.
    """

    summary: str
    description: str
    status: IssusStatus

    def build(request: Request) -> 'IssueCreateRequest':
        """
        Builds an IssueCreateRequest object from the provided Flask request.

        Args:
            request (Request): The Flask request object that contains the form data.

        Returns:
            IssueCreateRequest: A populated IssueCreateRequest instance.

        Raises:
            ArgumentError: If the required 'summary' or 'description' are missing or invalid.
        """
        model: IssueCreateRequest =  IssueCreateRequest(
            request.form.get('summary'),
            request.form.get('description'),
            IssusStatus.NEW
        )
        model.verify()
        return model
    
    def verify(self) -> None:
        """
        Verifies the validity of the 'summary' and 'description' fields.

        Raises:
            ArgumentError: If either the 'summary' or 'description' fields are empty.
        """
        if not self.summary: raise ArgumentError("summary", "not a valid summary input")
        if not self.description: raise ArgumentError("description", "not a valid description input")


@dataclass
class AddCommentRequest:
    """
    Represents a request to add a comment to an existing issue.

    Attributes:
        issue_id (int): The unique identifier of the issue.
        comment (str): The text of the comment to be added to the issue.

    Methods:
        build(request: Request) -> 'AddCommentRequest':
            Builds an AddCommentRequest instance from a Flask request.
        
        verify() -> None:
            Validates the required fields for the comment request.
    """

    issue_id: int
    comment: str

    def build(request: Request) -> 'AddCommentRequest':
        """
        Builds an AddCommentRequest object from the provided Flask request.

        Args:
            request (Request): The Flask request object containing the form data.

        Returns:
            AddCommentRequest: A populated AddCommentRequest instance.

        Raises:
            ArgumentError: If the 'comment' field is missing or invalid.
        """
        model: AddCommentRequest =  AddCommentRequest(
            int(request.form.get('issue_id')),
            request.form.get('comment')
        )
        model.verify()
        return model
    
    def verify(self) -> None:
        """
        Verifies the validity of the 'comment' field.

        Raises:
            ArgumentError: If the 'comment' field is empty.
        """
        if not self.comment: raise ArgumentError("comment", "not a valid comment input")


@dataclass
class UpdateIssueRequest:
    """
    Represents a request to update the status of an existing issue.

    Attributes:
        issue_id (int): The unique identifier of the issue.
        status (IssusStatus): The new status to set for the issue.

    Methods:
        build(request: Request) -> 'UpdateIssueRequest':
            Builds an UpdateIssueRequest instance from a Flask request.
    """

    issue_id: int
    status: IssusStatus

    def build(request: Request) -> 'UpdateIssueRequest':
        """
        Builds an UpdateIssueRequest object from the provided Flask request.

        Args:
            request (Request): The Flask request object containing the form data.

        Returns:
            UpdateIssueRequest: A populated UpdateIssueRequest instance.
        """
        model: UpdateIssueRequest =  UpdateIssueRequest(
            int(request.form.get('issue_id')),
            IssusStatus.of(request.form.get('status'))
        )
        return model