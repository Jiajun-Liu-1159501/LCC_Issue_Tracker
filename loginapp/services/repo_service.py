from loginapp import T, get_connection
from loginapp.model.data_model import User
from mysql.connector import cursor

class RepoService:

    def get_user_by_id(self, user_id: int, cur: cursor.MySQLCursor) -> User:
        if not cur:
            cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        cur.execute("SELECT * FROM users WHERE user_id = %s", [user_id])
        return User.of(cur.fetchone())