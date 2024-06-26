import pytest
from data.db_provider import DbProvider
from model.user import User
from repository.user_repository import UserRepository
from configuration import PSQL_PASSWORD


@pytest.fixture()
def db():
    db_provider = DbProvider(
        database='cross_shooting',
        user='postgres',
        password=PSQL_PASSWORD,
        autocommit=False
    )
    db_provider.begin()
    yield db_provider
    db_provider.rollback()


class TestUserRepository:

    def test_create(self, db):     
        user = User()
        user.id = 3
        user.state_id = 1
        user.is_admin = False
        user.is_true_admin = False

        repository = UserRepository(db)
        repository.create(user)
        users = db.execute_read_query('''SELECT * FROM users''')
        created_user = repository.read_by_id(user.id)

        assert len(users) == 3
        assert created_user.id == user.id
        assert created_user.state_id == user.state_id
        assert created_user.is_admin == user.is_admin
        assert created_user.is_true_admin == user.is_true_admin

    def test_update(self, db):
        user = User()
        user.id = 1
        user.state_id = 3
        user.is_admin = True
        user.is_true_admin = False

        repository = UserRepository(db)
        repository.update(user)
        updated_user = repository.read_by_id(user.id)

        assert updated_user.id == user.id
        assert updated_user.state_id == user.state_id
        assert updated_user.is_admin == user.is_admin
        assert updated_user.is_true_admin == user.is_true_admin
