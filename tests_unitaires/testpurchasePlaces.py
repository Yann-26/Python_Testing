import unittest
from flask import request, flash, render_template
from server import app, competitions, clubs

class TestPurchasePlaces(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_purchasePlaces(self):
        # DONNÉES FICTIVES POUR LA REQUÊTE POST
        data = {
            'competition': 'Spring Festival',
            'club': 'Iron Temple',
            'places': '2'
        }

        # APPEL DE LA ROUTE PURCHASEPLACES AVEC LES DONNÉES FICTIVES DE TEST
        response = self.app.post('/purchasePlaces', data=data, follow_redirects=True)

        # VÉRIFIER SI UN MESSAGE FLASH EST PRÉSENT
        self.assertIn(b'Error', response.data)

        # VÉRIFIER SI WELCOME RENVOIE LES BONNES DONNÉES
        self.assertEqual(response.status_code, 200)
