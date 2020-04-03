import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_ticker_table()

    def create_ticker_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "ticker_watchlist" (
          id INTEGER PRIMARY KEY,
          ticker TEXT,
          description TEXT,
          chose_ind boolean,
          created_date Date DEFAULT CURRENT_DATE,
          updated_date Date
        );
        """

        self.conn.execute(query)
