# Arkkitehtuurikuvaus

## Rakenne

![Pakettikaavio](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Pakkauskaavio.png)

Sovelluksella on referenssisovellusta muistuttava rakenne.

Pakkaus *ui* käsittelee käyttöliittymää eli koneen sisäisen toiminnon ja käyttäjän välistä vuorovaikutusta, *services* sovelluslogiikkaa, *entities* sovelluksen tietokohteita sekä *repositories* tietojen pysyväistallennusta.

## Käyttöliittymä
Käyttöliittymällä on seitsemän näkymää:
* Aloitusnäyttö
* Pelisäännöt
* Peliohjeet
* Vanhat pistetulokset
* Uuden tuloksen tallentaminen
* Pelaaminen
* Pause-näyttö

Näkymien näyttämisestä vastaa luokka ```Renderer```. Näppäimistön syötteistä vastaa luokat ``EventQueue`` ja ``EventHandler``. Nämä luokat sijaitsevat pakkauksessa ``ui``.

## Sovelluslogiikka
Sovelluksen loogisen tietomallin muodostavat luokat *Gameloop*, *Block* ja *Field*. *Block* käsittelee laskeutuvia palikoita, *Field* käsittelee ruudukkoa sekä jo laskeutuneita palikoita ja *Gameloop* kokoaa nämä yhteen.

![Luokkakaavio_sovelluslogiikka](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/arkkitehtuuri-sovelluslogiikka_luokkakaavio.png)

Luokalla ``Block`` on jokaisen mahdollisen palikkatyypin asennot kolminkerroksisessa taulukossa *shapes*. *block_type* määrittää laskeutuvan palikan muodon. 
*block_typen* arvo muuttuu ainoastaan silloin, kun ruudukkoon ilmestyy uusi palikka. *block_orientation* määrittää laskeutuvan palikan asennon, ja se muuttuu, 
pelaajan näppäinsyötteen perusteella. Attribuutit *shape*, *row* ja *column* määrittävät laskeutuvan palikan kunkin osan koordinaatit ruudukolla.

Luokan ``Block`` metodit ovat seuraavat:
* `move(direction)` - liikuttaa palikan määrättyyn suuntaan
* `movable(field, direction)` - palauttaa True, jos palikan pystyy liikuttamaan määrättyyn suuntaan
* `stop(field)` - palauttaa uuden ruudukon taulukkona, jossa laskeutunut palikka on tallennettu ruudukkoon
* `rotate(direction)` - muuttaa palikan asennon myötä- tai vastapäivään
* `rotatable(field, direction)` - palauttaa True, jos palikan asennon pystyy muuttamaan määrättyyn suuntaan
* `check_game_over(field)` - palauttaa True, jos uusi palikka ei mahdu enää ruudukkoon ja pelikierros loppuu

Luokka ``Field`` ylläpitää ruudukkoa, jossa laskeutuneiden palikkojen koordinaatit ovat tiedossa.

Luokan ``Field`` metodit ovat seuraavat:
* `get_field()` - palauttaa ruudukon taulukkona
* `update(new_field)` - muuttaa nykyisen ruudukon parametrina annettuun ruudukkoon
* `empty_filled_rows()` - palauttaa tyhjennettyjen rivien lukumäärän
* `check_filled_rows()` - palauttaa True, jos ruudukosta löytyy täydennettyjä rivejä

## Tietojen pysyväistallennus
Tietojen pysyväistallenuksesta vastuussa on pakkauksen *repositories* luokka ``ScoreRepository``. Luokka käsittelee pelituloksia pelaajanimineen SQLite tietokannassa. Luokka noudattaa Repository-suunnittelumallia.

Tietokannassa on taulu ``Scores``, jossa on sarakkeet ``name`` ja ``score``. Luokka ``ScoreRepository`` pystyy lisäämään uusia rivejä tauluun, hakea kymmenen riviä korkeimman pelituloksen mukaan sekä poistaa taulun ``Scores`` kaikki rivit.

Tietokannan tiedoston nimi määritellään projektin juurihakemiston tiedostossa ![.env](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/.env).

## Päätoiminnallisuudet
### Näkymien väliset siirtymiset

Sovelluksen käynnistäessä pelaaja on aina alkunäkymässä. Näkymien väliset siirtymiset alkavat luokasta ``Game``. 
Jokaiselle näkymälle on oma luokkansa, joiden nimien perässä on aina sana "View". 
Näkymät piirretään näytölle, kun luokka ``Game`` kutsuu luokan ``Renderer`` metodeja, jotka kutsuvat käyttäjän haluaman näkymän luokan metodeja.

![Näkymien_siirto](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/arkkitehtuuri-sekvenssikaavio_nakymien_valiset_siirtymiset.png)


### Tietokannan tietojen käsittely

#### Uuden pelikierroksen tuloksen tallentaminen

Pelaajan painaessa Enter-näppäintä aloitusnäkymässä, alkaa uusi pelikierros. Pelikierroksen päätyttyä pelaajalta kysytään pelaajanimi, jonka jälkeen sovellus palauttaa tuplen, jonka ensimmäisessä indeksissä on pelaajanimi ja toisessa pelitulos. Tuple annetaan syötteenä luokan ``ScoreRepository`` metodiin ``add_new_score``.

![Sekvenssikaavio_pelituloksen_tallentaminen](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/arkkitehtuuri-uuden_pelikierroksen_tuloksen_tallentaminen.png)

### Tietokannan tietojen poistaminen

Pelaajan painaessa näppäintä 3 aloitusnäkymässä, näkymä siirtyy parhaimpien pelituloksien näkymään. Kun pelaaja painaa D-näppäintä tässä näkymässä, metodi ``handle_menu_events()`` palauttaa "DELETE", jonka jälkeen pelaajalta varmistetaan ennen tietojen poistamista tietokannasta. Jos pelaaja painaa Y-näppäintä, metodi ``ensure_deleting()`` palauttaa True ja tiedot poistetaan tietokannasta. Jos pelaaja painaa N-näppäintä, metodi ``ensure_deleting()`` palauttaa False ja tiedot pysyvät tallessa.

![Sekvenssikaavio pelituloksien poistaminen](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/arkkitehtuuri-poista_tiedot_tietokannasta.png)

### Pelin aikaset tapahtumat

#### Palikan tippuminen
Palikka tippuu ruudukon verran alaspäin, kun palikan alapuolella ei ole muita palikoita tai ruudukon pohja sekä tapahtumasarja on tyhjä eli näppäimistöstä ei ole tullut käskyjä.

![Sekvenssikaavio_palikan_tippuminen](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Palikan%20tippuminen.png)

#### Palikan liikuttaminen
Palikan voi liikuttaa oikealle, vasemmalle tai alas, kun määrätyn suunnan kohteessa ei ole toista palikkaa tai seinää.

Suunta syötetään tuplena: oikea (0, 1), vasen (0, -1), alas (1, 0).

![Palikan_liikuttaminen_oikealle](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Palikan%20liikuttaminen%20oikealle.png)

Palikan asennon muuttaminen tapahtuu samalla logiikalla. Erona on se, että syötteenä annetaan kokonaisluku tuplen sijasta: myötäpäivään 1, vastapäivään -1.

#### Pisteen lisäys

Kun ruudukossa havaitaan täytettyjä rivejä, ne poistetaan ruudukosta, poistetuista riveistä ylemmät rivit tuodaan yhden ruudun verran alaspäin, ruudukon ylimmät 
tyhjät kohdat täytetään tyhjillä riveillä ja lopuksi lisätään poistettujen rivien määrä pelitulokseen.

![Pisteiden lisäys](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/arkkitehtuuri-sekvenssikaavio_pisteen_lisays.png)

#### Pelin loppuminen

Uuden palikan luodessa tarkistetaan, mahtuuko palikka ruudukkoon. Jos ei, peli päättyy.

![Pelin_loppuminen](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/arkkitehtuuri-pelin_loppuminen.png)

## Ohjelman rakenteeseen jääneet heikkoudet

* Ruudukko on määritelty tiedostossa ``game.py``, jonka olisi voinut toteuttaa tiedostosta lukemisena.
