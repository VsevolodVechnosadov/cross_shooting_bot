from model.user import User
from data.db_provider import DbProvider
from mapping.user_mapping import user_from_row


class UserRepository:
    
    def __init__(self, db_provider: DbProvider):
        self.db_provider = db_provider


    def create(self, user: User):
        self.db_provider.execute_query(
            '''INSERT INTO users (id, state_id, is_admin, is_true_admin) VALUES (%s, %s, %s, %s)''',
            (
                user.id,
                user.state_id,
                user.is_admin,
                user.is_true_admin,
            )
        )
   
    def read_by_id(self, id: int) -> User:
        rows = self.db_provider.execute_read_query(
            '''SELECT * FROM users WHERE id = %s''',
            (id,)
        )
        return user_from_row(rows[0])

    def update(self, user: User):
        self.db_provider.execute_query(
            '''UPDATE users SET state_id = %s, is_admin = %s WHERE id = %s''', 
            (
                user.state_id,
                user.is_admin,
                user.id,
            )
        )   
