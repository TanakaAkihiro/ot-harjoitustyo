from initialize_database import initialize_database


def build():
    '''Funktio, joka alustaa tietokannan. Funktio tulee kutsua ennen sovelluksen ensimmäistä käyttöä
    '''
    initialize_database()


if __name__ == "__main__":
    build()
