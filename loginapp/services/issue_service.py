from typing import Any, List
from loginapp import get_connection
from loginapp.model.issue_req_model import IssueCreateRequest
from mysql.connector import cursor

class IssueService:
    
    def create_issue(self, req: IssueCreateRequest, user_id: int) -> None:
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        cur.execute("INSERT INTO issues (user_id, summary, description, status) VALUES (%s, %s, %s, %s)", [user_id, req.summary, req.description, req.status.value])


    def list_issues(self) -> None:
        pass

    def all_issues(self, summary: str, user_name: str, user_id: str) -> None:
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        query_statement: str = "SELECT a.*, b.* FROM issues a LEFT JOIN users b ON a.user_id = b.user_id "
        where_statement: List[str] = []
        query_args: List[Any] = []
        if any(s for s in [query_statement, where_statement, query_args]):
            query_statement += "WHERE "
            if summary:
                where_statement.append("a.summary LIKE %s ")
                query_args.append(f"%{summary}%")
            if user_name: 
                where_statement.append("b.user_name LIKE %s ")
                query_args.append(f"%{user_name}%")
            if user_id:
                where_statement.append("a.user_id LIKE %s ")
                query_args.append(f"%{user_id}%")
            query_statement += "AND ".join(where_statement)
        cur.execute(query_statement + "ORDER BY issue_id DESC;", query_args)
        