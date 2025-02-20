from loginapp import get_connection
from loginapp.model.issue_req_model import IssueCreateRequest
from mysql.connector import cursor

class IssueService:
    
    def create_issue(self, req: IssueCreateRequest, user_id: int) -> None:
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        cur.execute("INSERT INTO issues (user_id, summary, description, status) VALUES (%s, %s, %s, %s)", [user_id, req.summary, req.description, req.status.value])


    def list_issues(self) -> None:
        pass