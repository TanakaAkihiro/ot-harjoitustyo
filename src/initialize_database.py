from database_connection import get_database_connection


def drop_tables(connection):
    '''Poistaa tiedot tietokannasta
    '''
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE if exists Scores
    ''')

    connection.commit()


def create_tables(connection):
    '''Luo tietokantaan taulun Scores, jossa sarakkeet name ja score
    '''
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE Scores (
            name TEXT,
            score INT
        )
    ''')

    connection.commit()


def initialize_database():
    '''Poistaa vanhat tiedot ja luo uuden taulun tietokantaan
    '''
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
