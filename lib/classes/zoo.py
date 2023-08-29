from lib import CONN, CURSOR

class Zoo:

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"Zoo(id={self.id}, name={self.name})"

    @classmethod
    def create_table(cls):
        sql="""CREATE TABLE IF NOT EXISTS zoos (
        id INTEGER PRIMARY KEY,
        name TEXT
        )
        """

        CURSOR.execute(sql)
