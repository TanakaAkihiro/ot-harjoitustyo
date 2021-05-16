# Testausdokumentti
## Yksikkö ja integraatiotestaus
Testauksiin on hyödynnetty unittestiä.
### Sovelluslogiikka
Sovelluslogiikasta vastaavien luokkien ``Gameloop``, ``Block`` ja ``Field`` testiluokat ovat ``TestGameloop``, ``TestBlock`` ja ``TestField``.

Testiluokassa ``TestGameloop`` hyödynnetään riippuvuuksien injektoinnin tekniikkaa. ``TestGameloop``in konstrukstoriin syötetään valeluokat ``StubClock``, ``StubEvent``,
``StubEventQueue``, ``StubEventHandler``, ``StubRenderer``, ``StubBlock``, ``StubBlockSetter`` ja ``StubField``.

### Repositorio-luokka
Sovelluksen repositorio-luokan ``ScoreRepository`` testiluokka on ``TestScoreRepository``. Tietokannan tiedoston nimi on määritelty projektin juuren ``.env.test``-tiedostoon.

### Testikattavuus
Testauskattavuus on 98% ilman käyttöliittymä-paketin, hakemiston src tiedostojen ``build.py`` ja ``initialize_database.py`` sekä luokan ``Game`` koodeja.

![Testauskattavuus](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/testausdokumentti-haaraumakattavuus.png)

``build.py`` ja ``initialize_database.py`` koodeja on jätetty testaamatta, sillä tiedostoa näiden tiedostojen tehtävänä on alustaa tietokantaa.

Luokan ``Game`` testaaminen on jätetty pois, sillä sen metodi ``start_screen`` on ikuinen silmukka, sillä metodi kutsuu itsensä, jonka takia testaamisesta tulee hankalaa.
Lisäksi luokka ei käytä riippuvuuksien injektointia, jolloin metodin ``initialize`` testaaminen on myöskin hankalaa.

## Järjestelmätestaus

Järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja konfigurointi
Sovellusksen toimivuutta on testattu Linux-ympäristössä ![käyttöohjeen](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md) mukaisesti.

Sovellusta on testattu eri konfiguraatioilla muokkaamalla ``.env``-tiedostoa.

### Toiminnallisuudet

Sovellus noudattaa jokaista ![vaativuusmäärittelyssä](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md) esitettyjä 
päätoiminnallisuuden piirteitä. 

Mahdollisia "ilkeitä" syötteitä on testattu, kuten näppäinten painelua, jotka eivät esiinny missään ohjeissa.

## Sovellukseen jääneet laatuongelmat

Sovellus ei näytä järkeviä virheilmoituksia seuraavissa tapauksissa:

* kun sovellus käynnistetään ennen tietokannan alustamista komennolla ``poetry run invoke build``.
