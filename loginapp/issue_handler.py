
from flask import Blueprint

issue: Blueprint = Blueprint('issue', __name__)

@issue.post()
def create_issue_endpoint() -> str:
    pass