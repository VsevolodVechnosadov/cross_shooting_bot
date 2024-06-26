import psycopg2
from psycopg2 import OperationalError


class DbProvider:

    def __init__(self, database, user, password, autocommit=True):
        self.connection = psycopg2.connect(f'dbname={database} user={user} password={password}')
        self.comm = autocommit
    
    def execute_query(self, query, values=set()):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, values)
            if self.comm == True:
                self.connection.commit()
        except OperationalError as e:
            print(e)

    def execute_read_query(self, query, values=set()) -> list:
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, values)
            result = cursor.fetchall()
            return result
        except OperationalError as e:
            print(e)
    
    def begin(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('''BEGIN;''')
        except OperationalError as e:
            print(e)

    def rollback(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('''ROLLBACK;''')
        except OperationalError as e:
            print(e)
