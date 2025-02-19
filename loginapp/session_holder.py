
from dataclasses import asdict
from flask.sessions import SessionMixin
from loginapp.model.data_model import User
from loginapp.utils.concurrent_dict import ConcurrentDict
import hashlib, json, datetime

class SessionHolder:

    session_dict: ConcurrentDict[str, int] = ConcurrentDict()

    @staticmethod
    def session_hold(session: SessionMixin, user: User) -> None:
        token: str = SessionHolder.generate_token(user)
        SessionHolder.session_dict.setdefault(token, int(datetime.datetime.now().timestamp() * 1000))
        session.setdefault('token', token)
        session.setdefault('user', user)

    @staticmethod
    def session_evict(session: SessionMixin, user: User) -> None:
        if user == None:
            SessionHolder.session_dict.pop(session.pop('token', None))
            session.pop('user', None)
        else:
            token: str = SessionHolder.generate_token(user)
            SessionHolder.session_dict.pop(token, None)

    @staticmethod
    def generate_token(user: User) -> str:
        user_info = json.dumps(asdict(user), sort_keys = True)
        return hashlib.md5(user_info.encode()).hexdigest()