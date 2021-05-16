from database_connection import get_database_connection


class ScoreRepository:
    '''Luokka, joka käsittelee tietokannan toimntoja.

    Attributes:
        connection: Yhteys tietokantatiedostoon
    '''

    def __init__(self, connection):
        '''
        Args:
            connection: Yhteys tietokantatiedostoon
        '''
        self._connection = connection

    def find_high_scores(self):
        '''Hakee kymmenen parasta pelitulosta pelaajanimen kanssa

        Returns:
            Listan tupleja, joiden ensimmäisessä indeksissä on pelaajanimi ja toisessa pelitulos
        '''
        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM Scores ORDER BY score DESC LIMIT 10')

        high_scores = cursor.fetchall()

        return high_scores

    def delete_all(self):
        '''Poistaa tiedot tietokannasta
        '''
        cursor = self._connection.cursor()

        cursor.execute('DELETE FROM Scores')

        self._connection.commit()

    def add_new_score(self, name, score):
        '''Kirjaa uuden pelituloksen ja pelaajanimen tietokantaan
        '''
        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT INTO Scores (name, score) VALUES (?, ?)', (name, score))

        self._connection.commit()


score_repository = ScoreRepository(get_database_connection())
