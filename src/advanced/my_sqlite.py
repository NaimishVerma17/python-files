import sqlite3


class MySqlite:
    database_name = 'example_database'
    global conn, cursor, table_name

    def __init__(self, table_name):
        self.table_name = table_name
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS {} (id INTEGER PRIMARY KEY AUTOINCREMENT, task_name TEXT)
        '''.format(self.table_name)
        self.cursor.execute(query)

    def insert_data(self, task_name):
        query = 'INSERT INTO {} (task_name) VALUES (?)'.format(self.table_name)
        self.cursor.execute(query, (task_name,))
        self.conn.commit()

    def read_data(self):
        query = 'SELECT * FROM {}'.format(self.table_name)
        return self.cursor.execute(query)

    def close_connection(self):
        self.conn.close()
