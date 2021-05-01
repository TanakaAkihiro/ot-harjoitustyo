# Arkkitehtuurikuvaus

## Rakenne

![Pakettikaavio](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Pakkauskaavio.png)

## Päätoiminnallisuudet

### Palikoiden liikkeet

#### Tippuminen
Palikka tippuu ruudukon verran alaspäin, kun palikan alapuolella ei ole muita palikoita tai ruudukon pohja sekä tapahtumasarja on tyhjä eli näppäimistöstä ei ole tullut käskyjä.

![Sekvenssikaavio_palikan_tippuminen](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Palikan%20tippuminen.png)

#### Liikuttaminen
Palikan voi liikuttaa oikealle, vasemmalle tai alas, kun määrätyn suunnan kohteessa ei ole toista palikkaa tai seinää.

Suunta annetaan tuplena: oikea (0, 1), vasen (0, -1), alas (1, 0).

![Palikan_liikuttaminen_oikealle](https://github.com/TanakaAkihiro/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/Palikan%20liikuttaminen%20oikealle.png)
