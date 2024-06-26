import psycopg2
from psycopg2 import OperationalError

from connection import connection


def execute_read_query(query, values=set()):
    cursor = connection.cursor()
    try:
        cursor.execute(query, values)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(e)
