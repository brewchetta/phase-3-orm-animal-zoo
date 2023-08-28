from lib import CONN, CURSOR

class Animal:

    # THIS METHOD WILL CREATE THE SQL TABLE AND IS GIVEN TO YOU #
    @classmethod
    def create_table(cls):
        create_animals_sql = """CREATE TABLE IF NOT EXISTS animals (
        id INTEGER PRIMARY KEY, name TEXT, age INTEGER
        )
        """
        CURSOR.execute(create_animals_sql)


    # ADD YOUR CODE BELOW #
