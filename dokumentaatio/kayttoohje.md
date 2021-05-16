# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:
```
poetry install
```
Alusta sitten tietokanta komennolla:
```
poetry run invoke build
```
Käynnistä ohjelma komennolla:
```
poetry run invoke start
```
## Alkunäkymä

Alkunäkymässä voit tehdä neljä toimintoa:


1. Aloita uusi pelikierros
2. Lue pelisäännöt
3. Lue pelin ohjeet
4. Tarkastele/tyhjennä pistetaulua, jossa on edellisten pelaajien pistetulokset

![Alkunäkymä](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kayttoohje-alkunakyma.png)

Alkunäkymään voi palata painamalla R-näppäintä.

**Pelisäännöt**
![Pelisäännöt](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kayttoohje-pelisaannot.png)
**Pelin ohjeet**
![Peliohjeet](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kayttoohje-peliohjeet.png)
**Vanhat pelitulokset**
![Vanhat pelitulokset](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kayttoohje-vanhat_tulokset.png)
*Varmistus ennen tietojen poistamista*
![Varmistus](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kayttoohje-varmistus.png)

## Pelin aikana

Pelaaja voi liikuttaa palikoita nuolinäppäimillä oikealle(→-key), vasemmalle(←-key) ja ruudukon verran alaspäin(🠃-key).

Pelaaja voi muuttaa palikan suuntaa myötäpäivään(🠁-key) sekä vastapäivään(z-key).

![Pelinäkymä](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kayttoohje-pelinakyma.png)

Pelaaja voi tauottaa pelaamisen panamalla P-näppäintä

![Pause-näyttö](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kayttoohje-pause.png)

## Pelin loppuessa

Pelaaja voi näppäillä nimen, jotta pistetulos tallennetaan tiedostoon.
