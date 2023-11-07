import psycopg2
import psycopg2.extensions


class DataBaseConnector:
    connection: psycopg2.extensions.connection
    cursor: psycopg2.extensions.cursor

    def __init__(self, dbname, user, password, host, port):
        self.connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

    def fetchData(self, sql_request: str):
        self.cursor = self.connection.cursor()
        self.cursor.execute(sql_request)
        data = self.cursor.fetchall()
        self.cursor.close()
        return data

    def sqlRequest(self, sql_request: str):
        self.cursor = self.connection.cursor()
        self.cursor.execute(sql_request)
        self.connection.commit()
        self.cursor.close()
