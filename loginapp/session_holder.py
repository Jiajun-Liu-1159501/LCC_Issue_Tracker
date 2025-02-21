
from dataclasses import asdict
import re
from flask import session
from flask.sessions import SessionMixin
from loginapp.constant.user_role import Role
from loginapp.model.data_model import User
from loginapp.utils.concurrent_dict import ConcurrentDict
import hashlib, json, datetime

class SessionHolder:
    """
    A utility class for managing user sessions in a Flask application.

    This class provides static methods for handling session persistence, 
    eviction, and validation. It uses a thread-safe `ConcurrentDict` to store 
    active sessions, preventing conflicts in concurrent environments.

    Attributes:
        session_dict (ConcurrentDict[str, int]): A dictionary to store session 
        timestamps, mapping session tokens to their creation time.

    Example:
        ```python
        session_holder = SessionHolder()
        session_holder.session_hold(flask_session, user)
        if session_holder.session_exists("some_token"):
            print("Session is valid")
        ```
    """

    session_dict: ConcurrentDict[str, User] = ConcurrentDict()

    @staticmethod
    def session_hold(session: SessionMixin, user: User) -> None:
        """
        Creates and stores a session for the given user.

        Generates a unique token for the user and stores it in both the 
        `session_dict` and the Flask session object.

        Args:
            session (SessionMixin): The Flask session object.
            user (User): The user object representing the logged-in user.

        Example:
            ```python
            SessionHolder.session_hold(session, user)
            ```
        """
        token: str = SessionHolder.generate_token(user)
        SessionHolder.session_dict.setdefault(token, user)
        session.setdefault('token', token)

    @staticmethod
    def session_evict(session: SessionMixin, user: User) -> None:
        """
        Removes a user session from the system.

        If a user is provided, their specific session token is removed.
        If no user is provided, the currently stored session token is deleted.

        Args:
            session (SessionMixin): The Flask session object.
            user (Optional[User]): The user to evict, or None to remove the current session.

        Example:
            ```python
            SessionHolder.session_evict(session, user)
            ```
        """
        if user == None:
            SessionHolder.session_dict.pop(session.pop('token', None))
        else:
            token: str = SessionHolder.generate_token(user)
            SessionHolder.session_dict.pop(token, None)

    @staticmethod
    def current_login() -> User:
        """
        Retrieves the currently logged-in user from the session.

        Returns:
            Optional[User]: The user object if a session exists, otherwise None.

        Example:
            ```python
            user = SessionHolder.current_login()
            if user:
                print(f"Logged in as {user.username}")
            ```
        """
        return SessionHolder.session_dict.get(session.get('token'), None)
    
    @staticmethod
    def session_exists(token: str) -> bool:
        """
        Checks if a session token exists.

        Args:
            token (str): The session token to check.

        Returns:
            bool: True if the session token exists, otherwise False.

        Example:
            ```python
            if SessionHolder.session_exists("some_token"):
                print("Session is valid")
            ```
        """
        return session.get('token') != None

    @staticmethod
    def generate_token(user: User) -> str:
        """
        Generates a unique session token for a user.

        The token is generated as an MD5 hash of the JSON-serialized user object.

        Args:
            user (User): The user object to generate a token for.

        Returns:
            str: A unique session token.

        Example:
            ```python
            token = SessionHolder.generate_token(user)
            print(f"Generated Token: {token}")
            ```
        """
        user_info = json.dumps(asdict(user), sort_keys = True)
        return hashlib.md5(user_info.encode()).hexdigest()