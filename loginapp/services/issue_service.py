from typing import Any, Callable, Dict, List
from loginapp import T, get_connection
from loginapp.constant.issue_status import IssusStatus
from loginapp.constant.user_role import Role
from loginapp.model.data_model import User
from loginapp.model.issue_req_model import AddCommentRequest, IssueCreateRequest
from mysql.connector import cursor

class IssueService:
    """
    Service class for handling issue-related database operations.
    Provides methods to create, retrieve, update, and comment on issues.
    """

    
    def get_user_by_id(self, user_id: int, cur: cursor.MySQLCursor) -> User:
        """
        Retrieves a user from the database based on the given user ID.
        
        Args:
            user_id (int): The ID of the user to retrieve.
            cur (cursor.MySQLCursor): The active database cursor.
        
        Returns:
            User: An instance of the User model containing user details.
        """
        if not cur:
            cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        cur.execute("SELECT * FROM users WHERE user_id = %s", [user_id])
        return User.of(cur.fetchone())
    
    
    def create_issue(self, req: IssueCreateRequest, user_id: int) -> None:
        """
        Inserts a new issue into the database.
        
        Args:
            req (IssueCreateRequest): The issue request object containing issue details.
            user_id (int): The ID of the user creating the issue.
        
        Returns:
            None
        """
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        cur.execute("INSERT INTO issues (user_id, summary, description, status) VALUES (%s, %s, %s, %s);", [user_id, req.summary, req.description, req.status.value])

    
    def all_issues(self, summary: str, user_name: str, user_id: str, convert: Callable[[Dict[str, Any]], T]) -> List[T]:
        """
        Retrieves all issues, optionally filtered by summary, user name, or user ID.
        
        Args:
            summary (str): A keyword to filter issues by summary.
            user_name (str): A keyword to filter issues by user name.
            user_id (str): The ID of the user to filter issues by.
            convert (Callable[[Dict[str, Any]], T]): A function to map database records to response models.
        
        Returns:
            List[T]: A list of converted issue records.
        """
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
                where_statement.append("a.user_id = %s ")
                query_args.append(user_id)
            query_statement += "AND ".join(where_statement)
        query_statement += "GROUP BY a.issue_id, b.user_id ORDER BY a.created_at DESC;"
        cur.execute(query_statement, query_args)
        issue_dict: Dict[str, Any] = cur.fetchall()
        return issue_dict if not convert else list(map(lambda x: convert(x), issue_dict))

    
    def issue_detail(self, issue_id: int, function: Callable[[Dict[str, Any], List[Dict[str, Any]]], T]) -> T:
        """
        Retrieves detailed information about a specific issue, including comments.
        
        Args:
            issue_id (int): The ID of the issue to retrieve.
            function (Callable[[Dict[str, Any], List[Dict[str, Any]]], T]): A function to format the result.
        
        Returns:
            T: The formatted issue details.
        """
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        query_statement: str = "SELECT a.issue_id, a.summary, a.description, a.created_at, a.status, b.user_id, b.user_name, b.profile_image FROM issues a LEFT JOIN users b ON a.user_id = b.user_id WHERE a.issue_id = %s;"
        cur.execute(query_statement, [issue_id])
        issue: Dict[str, Any] = cur.fetchone()
        comment_statement: str = "SELECT a.comment_id, a.content, a.created_at, b.user_id, b.user_name, b.profile_image, b.role FROM comments a LEFT JOIN users b ON a.user_id = b.user_id WHERE a.issue_id = %s ORDER BY a.created_at ASC;"
        cur.execute(comment_statement, [issue_id])
        comments: List[Dict[str, Any]] = cur.fetchall()
        return function(issue, comments)
    
    
    def add_comment(self, user_id: int, req: AddCommentRequest) -> None:
        """
        Adds a comment to an issue and updates the issue status if necessary.
        
        Args:
            user_id (int): The ID of the user adding the comment.
            req (AddCommentRequest): The comment request object.
        
        Returns:
            None
        """
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        user: User = self.get_user_by_id(user_id, cur)
        cur.execute("INSERT INTO comments (issue_id, user_id, content) VALUES (%s, %s, %s);", [req.issue_id, user_id, req.comment])
        if user.get_role_enum() is Role.VISITOR:
            return
        self.update_issues(req.issue_id, IssusStatus.OPEN.value, cur)

    
    def update_issues(self, issue_id: int, status: str, cur: cursor.MySQLCursor) -> None:
        """
        Updates the status of an issue in the database.
        
        Args:
            issue_id (int): The ID of the issue to update.
            status (str): The new status value.
            cur (cursor.MySQLCursor): The active database cursor.
        
        Returns:
            None
        """
        if not cur:
            cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        cur.execute("UPDATE issues SET status = %s WHERE issue_id = %s;", [status, issue_id])

