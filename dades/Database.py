#https://stackoverflow.com/questions/38076220/python-mysqldb-connection-in-a-class
import mysql.connector

class Database:

    def __init__(self,p_host="localhost",p_user="root",p_password="",p_dbname="montilivi"):
        self.host=p_host
        self.user=p_user
        self.password=p_password
        self.dbname=p_dbname

        self._conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.dbname
        )

        self._conn.autocommit = False
        self._cursor = self._conn.cursor(dictionary=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._close()

    def connection(self):
        return self._conn

    def cursor(self):
        return self._cursor
    
    def _close(self):
        self._conn.close()
    
    def execute(self, sql, params=None):
        self._cursor.execute(sql, params or ())

    def commit(self):
        self._conn.commit()

    def fetchall(self):
        return self._cursor.fetchall()

    def fetchone(self):
        return self._cursor.fetchone()

    def query(self, sql, params=None):
        self._cursor.execute(sql, params or ())
        return self.fetchall()        

    @staticmethod
    def test_connection():
        try:
            db= Database()
            db.execute('SELECT VERSION()')
            version=db.fetchone()
            print('Connexió correcte a la base de dades.')
            print(version)
        except:
            print('Error en connectar a la base de dades')
