# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi.

## Ohjelman käynnistäminen

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla:
```
poetry install
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

Alkunäkymään voi palautua painamalla R-näppäintä.

![Alkunäkymä](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/kayttoohje-alkunaytto.png)

## Pelin aikana

Pelaaja voi liikuttaa palikoita nuolinäppäimillä oikealle(→-key), vasemmalle(←-key) ja ruudukon verran alaspäin(🠃-key).

Pelaaja voi muuttaa palikan suuntaa myötäpäivään(🠁-key) sekä vastapäivään(z-key).

## Pelin loppuessa

Pelaaja voi näppäillä nimen, jotta pistetulos tallennetaan tiedostoon.
