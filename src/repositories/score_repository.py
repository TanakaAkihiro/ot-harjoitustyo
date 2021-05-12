from database_connection import get_database_connection


class ScoreRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def find_ranking(self):
        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM Scores ORDER BY score DESC LIMIT 10')

        ranking = cursor.fetchall()

        return ranking

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute('DELETE FROM Scores')

        self._connection.commi()

    def add_new_score(self, name, score):
        cursor = self._connection.cursor()
        
        cursor.execute('INSERT INTO Scores (name, score) VALUES (?, ?)', (name, score))

        self._connection.commit()

score_repository = ScoreRepository(get_database_connection())