import psycopg2
from psycopg2 import OperationalError

from configuration import PSQL_PASSWORD


def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            database='cross_shooting',
            user='postgres',
            password=PSQL_PASSWORD,
            host='127.0.0.1',
            port='5432',
        )
    except OperationalError as e:
        print(e)
    return connection

connection = create_connection()
    