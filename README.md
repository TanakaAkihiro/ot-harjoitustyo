# Tetris

Perinteinen tietokonepeli, jota kaikki on varmasti kerran nähnyt tai pelannut.

## Huomio Python-versiosta

Sovellukseen vaaditaan Python-versio 3.7.0 tai uudempi versio. Sovellus silti saattaa toimia myös vanhemmallakin versiolla.

## Dokumentaatio  

[Vaatimusmäärittely](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/laskarit/alustava_maarittelydokumentti.md)

[Työaikakirjanpito](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/tetris/dokumentaatio/tuntikirjanpito.md)

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```
poetry run invoke start
```

###Testaus

Testit suoritetaan komennolla:

```
poetry run invoke test
```

###Testikattavuus

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
