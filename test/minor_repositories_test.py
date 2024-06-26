from data.db_provider import DbProvider

from model.genre import Genre
from model.group import Group
from model.place import Place

from repository.genre_repository import GenreRepository
from repository.group_repository import GroupRepository
from repository.place_repository import PlaceRepository
from configuration import PSQL_PASSWORD


class TestGenreRepository:

    def test_read_all(self):
        db_provider = DbProvider(
            database='cross_shooting',
            user='postgres',
            password=PSQL_PASSWORD
        )
        genre_repository = GenreRepository(db_provider)
        genres = genre_repository.read_all()
        assert len(genres) == 3

    def test_read_by_id(self):
        db_provider = DbProvider(
            database='cross_shooting',
            user='postgres',
            password=PSQL_PASSWORD
        )
        genre_repository = GenreRepository(db_provider)

        genre_needed = genre_repository.read_by_id(1)
        assert genre_needed.name == 'Battle-Royal'

        genre_needed = genre_repository.read_by_id(2)
        assert genre_needed.name == 'King of the Mount'

        genre_needed = genre_repository.read_by_id(3)
        assert genre_needed.name == 'All Against All'

class TestGroupRepository:

    def test_read_all(self):
        db_provider = DbProvider(
            database='cross_shooting',
            user='postgres',
            password=PSQL_PASSWORD
        )
        group_repository = GroupRepository(db_provider)
        groups = group_repository.read_all()
        assert len(groups) == 4

    def test_read_by_id(self):
        db_provider = DbProvider(
            database='cross_shooting',
            user='postgres',
            password=PSQL_PASSWORD
        )
        group_repository = GroupRepository(db_provider)

        group_needed = group_repository.read_by_id(1)
        assert group_needed.name == 'Death Wolves'

        group_needed = group_repository.read_by_id(2)
        assert group_needed.name == 'Punkihoy'

        group_needed = group_repository.read_by_id(3)
        assert group_needed.name == 'Shoota Boyz'

        group_needed = group_repository.read_by_id(4)
        assert group_needed.name == 'Suicide Squad'

class TestPlaceRepository:

    def test_read_all(self):
        db_provider = DbProvider(
            database='cross_shooting',
            user='postgres',
            password=PSQL_PASSWORD
        )
        place_repository = PlaceRepository(db_provider)
        places = place_repository.read_all()
        assert len(places) == 4

    def test_read_by_id(self):
        db_provider = DbProvider(
            database='cross_shooting',
            user='postgres',
            password=PSQL_PASSWORD
        )
        place_repository = PlaceRepository(db_provider)

        place_needed = place_repository.read_by_id(1)
        assert place_needed.name == 'Totskiy Polygon'

        place_needed = place_repository.read_by_id(2)
        assert place_needed.name == 'Opushka'

        place_needed = place_repository.read_by_id(3)
        assert place_needed.name == 'Kolpino'

        place_needed = place_repository.read_by_id(4)
        assert place_needed.name == 'Sanctum Peterium Hive'
