# Arkkitehtuurikuvaus

## Rakenne

![Pakettikaavio](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Pakkauskaavio.png)

Sovelluksella on referenssisovellusta muistuttava rakenne.

Pakkaus *ui* käsittelee käyttöliittymää eli koneen sisäisen toiminnon ja käyttäjän välistä vuorovaikutusta, 'services' sovelluslogiikkaa, 'entities' sovelluksen tietokohteita sekä 'repositories' tietojen pysyväistallennusta.

## Käyttöliittymä
Käyttöliittymällä on kuusi näkymää:
* Aloitusnäyttö
* Pelisäännöt
* Peliohjeet
* Vanhat pistetulokset
* Uuden tuloksen tallentaminen
* Pelaaminen

Näkymien näyttämisestä vastaa luokka *Renderer*. Näppäimistön syötteistä vastaa luokat *EventQueue* ja *EventHandler*. Nämä luokat sijaitsevat pakkauksessa *ui*.

## Sovelluslogiikka
Sovelluksen loogisen tietomallin muodostavat luokat *Gameloop*, *Block* ja *Field*. *Block* käsittelee laskeutuvia palikoita, *Field* käsittelee ruudukkoa sekä jo laskeutuneita palikoita ja *Gameloop* kokoaa nämä yhteen.

![Luokkakaavio_sovelluslogiikka](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/arkkitehtuuri-Sovelluslogiikka_Luokkakaavio.png)

Luokalla *Block* on jokaisen mahdollisen palikkatyypin asennot kolminkerroksisessa taulukossa *shapes*. *block_type* määrittää laskeutuvan palikan muodon. 
*block_typen* arvo muuttuu ainoastaan silloin, kun ruudukkoon ilmestyy uusi palikka. *block_orientation* määrittää laskeutuvan palikan asennon, ja se muuttuu, 
pelaajan näppäinsyötteen perusteella. Attribuutit *shape*, *row* ja *column* määrittävät laskeutuvan palikan kunkin osan koordinaatit ruudukolla.

Luokan *Block* metodit ovat seuraavat:
* `move(direction)`
* `movable(field, direction)`
* `stop(field)`
* `rotate(direction)`
* `rotatable(field, direction)`
* `check_game_over(field)`

Luokka *Field* ylläpitää ruudukkoa, jossa laskeutuneiden palikkojen koordinaatit ovat tiedossa.

## Päätoiminnallisuudet

### Palikoiden liikkeet

#### Tippuminen
Palikka tippuu ruudukon verran alaspäin, kun palikan alapuolella ei ole muita palikoita tai ruudukon pohja sekä tapahtumasarja on tyhjä eli näppäimistöstä ei ole tullut käskyjä.

![Sekvenssikaavio_palikan_tippuminen](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Palikan%20tippuminen.png)

#### Liikuttaminen
Palikan voi liikuttaa oikealle, vasemmalle tai alas, kun määrätyn suunnan kohteessa ei ole toista palikkaa tai seinää.

Suunta syötetään tuplena: oikea (0, 1), vasen (0, -1), alas (1, 0).

![Palikan_liikuttaminen_oikealle](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Palikan%20liikuttaminen%20oikealle.png)
