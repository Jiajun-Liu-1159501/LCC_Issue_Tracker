
from flask import session
from flask.sessions import SessionMixin
from loginapp.model.data_model import User
from loginapp.utils.concurrent_dict import ConcurrentDict
import hashlib, json

class SessionHolder:
    """
    Manages user authentication sessions by storing and retrieving session-related data.
    
    Attributes:
        session_dict (ConcurrentDict): A dictionary mapping session tokens to User objects.
        token_dict (ConcurrentDict): A dictionary mapping session tokens to session instances.
    """


    session_dict: ConcurrentDict[str, User] = ConcurrentDict()
    token_dict: ConcurrentDict[str, SessionMixin] = ConcurrentDict()

    @staticmethod
    def session_hold(session: SessionMixin, user: User) -> None:
        """
        Establishes a session for the given user.
        
        Args:
            session (SessionMixin): The Flask session object.
            user (User): The authenticated user object.
        """
        token: str = SessionHolder.generate_token(user)
        SessionHolder.session_dict.setdefault(token, user)
        SessionHolder.token_dict.setdefault(token, session)
        session.setdefault('token', token)

    @staticmethod
    def session_evict(session: SessionMixin, user: User) -> None:
        """
        Clears the session for the given user or the current session if no user is specified.
        
        Args:
            session (SessionMixin): The Flask session object.
            user (User): The user whose session needs to be evicted. If None, clears the current session.
        """
        if user == None:
            token: str = session.pop('token', None)
            SessionHolder.session_dict.pop(token, None)
            SessionHolder.token_dict.pop(token, None)
        else:
            token: str = SessionHolder.generate_token(user)
            SessionHolder.session_dict.pop(token, None)
            SessionHolder.token_dict.pop(token, None).pop('token', None)

    @staticmethod
    def current_login() -> User:
        """
        Retrieves the currently logged-in user based on the session token.
        
        Returns:
            User: The currently authenticated user, or None if no session exists.
        """
        return SessionHolder.session_dict.get(session.get('token'), None)
    
    @staticmethod
    def session_exists(token: str) -> bool:
        """
        Checks if a session exists for the given token.
        
        Args:
            token (str): The session token.
        
        Returns:
            bool: True if the session exists, False otherwise.
        """
        return session.get('token') != None

    @staticmethod
    def generate_token(user: User) -> str:
        """
        Generates a unique session token for a given user.
        
        Args:
            user (User): The user object for whom the token is generated.
        
        Returns:
            str: A hashed session token.
        """
        user_info = json.dumps({"user_id": user.user_id}, sort_keys = True)
        return hashlib.md5(user_info.encode()).hexdigest()