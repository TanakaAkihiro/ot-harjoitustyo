# Tetris

Perinteinen tietokonepeli, jota kaikki on varmasti kerran nähnyt tai pelannut.

## Huomio Python-versiosta

Sovellukseen vaaditaan Python-versio 3.7.0 tai uudempi versio. Sovellus silti saattaa toimia myös vanhemmallakin versiolla.

## Dokumentaatio
* [Käyttöohje](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

* [Vaatimusmäärittely](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

* [Arkkitehtuuri](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

* [Työaikakirjanpito](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/tetris/dokumentaatio/tuntikirjanpito.md)

## Asennus

Asenna riippuvuudet komennolla:
```
poetry install
```


## Komentorivitoiminnot
### Ohjelman alustaminen

Alusta tietokanta ohjelman suoritusta varten komennolla:

```
poetry run invoke build
```

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```
poetry run invoke coverage-report
```

Raportti generoituu *htmlcov*-hakemistoon.

### Pylint

Tiedoston .pylintrc määrittelemät tarkistukset voi suorittaa komennolla:

```
poetry run invoke lint
```

## Releases

[Viikko 5](https://github.com/TanakaAkihiro/ot-harjoitustyo/releases/tag/viikko5)

[Viikko 6](https://github.com/TanakaAkihiro/ot-harjoitustyo/releases/tag/viikko6)

[Viikko 7](https://github.com/TanakaAkihiro/ot-harjoitustyo/releases/tag/Loppupalautus)
