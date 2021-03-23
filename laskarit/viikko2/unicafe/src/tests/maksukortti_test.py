import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        self.maksukortti.syo.maukkaasti()
        self.maksukortti.syo.maukkaasti()
        self.maksukortti.syo.maukkaasti()
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 2 euroa")
    
    def test_ei_lataa_negatiivista_rahamaaraa(self):
        self.maksukortti.lataa_rahaa(-10)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10 euroa")
    
    def test_syo_edullisesti_vain_jos_rahaa_riittavasti(self):
        self.maksukortti.syo.edullisesti()
        self.maksukortti.syo.edullisesti()