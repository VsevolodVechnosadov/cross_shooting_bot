from model.user import User


def user_from_row(row: tuple) -> User:
    user = User()
    user.id = row[0]
    user.state_id = row[1]
    user.is_admin = row[2]
    user.is_true_admin = row[3]
    return user
