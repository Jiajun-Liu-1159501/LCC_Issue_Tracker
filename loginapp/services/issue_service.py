from typing import Any, Callable, Dict, List
from loginapp import T, get_connection
from loginapp.model.issue_req_model import IssueCreateRequest
from mysql.connector import cursor

class IssueService:
    
    def create_issue(self, req: IssueCreateRequest, user_id: int) -> None:
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        cur.execute("INSERT INTO issues (user_id, summary, description, status) VALUES (%s, %s, %s, %s)", [user_id, req.summary, req.description, req.status.value])


    def list_issues(self) -> None:
        pass

    def all_issues(self, summary: str, user_name: str, user_id: str, convert: Callable[[Dict[str, Any]], T]) -> List[T]:
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        query_statement: str = "SELECT a.issue_id, a.summary, a.created_at, a.status, b.user_id, b.user_name, b.profile_image, COUNT(c.comment_id) as comments FROM issues a LEFT JOIN users b ON a.user_id = b.user_id LEFT JOIN comments c ON c.issue_id = a.issue_id "
        where_statement: List[str] = []
        query_args: List[Any] = []
        if any(s for s in [summary, user_name, user_id]):
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
        query_statement += "GROUP BY a.issue_id, b.user_id ORDER BY a.created_at DESC;"
        print(query_statement)
        cur.execute(query_statement, query_args)
        issue_dict: Dict[str, Any] = cur.fetchall()
        return issue_dict if not convert else list(map(lambda x: convert(x), issue_dict))