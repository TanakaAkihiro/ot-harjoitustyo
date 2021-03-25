import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)
    
    def test_kassapaate_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassapaatteen_rahamaara_ja_myytyjen_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_toimii_kun_maksu_riittava_rahamaara_kassassa(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100640)

    def test_kateisosto_toimii_kun_maksu_riittava_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(1000), 600)
    
    def test_kateisosto_toimii_kun_maksu_riittava_myytyjen_lounaiden_maara_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 2)
    
    def test_kateisosto_toimii_kun_maksu_ei_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_korttiosto_toimii_kun_kortilla_tarpeeksi_rahaa_veloitetaan_summa_kortilta_ja_palautetaan_True(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))
        self.assertEqual(str(self.maksukortti),"saldo: 3.6" )
    
    def test_korttiosto_toimii_kun_kortilla_tarpeeksi_rahaa_myytyjen_lounaiden_maara_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 2)
    
    def test_korttiosto_toimii_kun_kortilla_ei_tarpeeksi_rahaa_kortin_saldo_pysyy_samana_myytyjen_lounaiden_maara_sama_palauta_False(self):
        maksukortti = Maksukortti(100)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(maksukortti))
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(maksukortti))
        self.assertEqual(str(maksukortti), "saldo: 1.0")
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)

    def test_korttiosto_ei_muuta_kassan_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_ladattaessa_kortin_saldo_kasvaa_ja_kassan_rahamaara_kasvaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")

    def test_kortille_ladattaessa_negatiivisen_summan_ei_tapahdu_mitaan(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")