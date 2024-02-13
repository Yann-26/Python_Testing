# import unittest
# from flask import request, flash, render_template
# from server import app, competitions, clubs

# class TestPurchasePlaces(unittest.TestCase):

#     def setUp(self):
#         app.config['TESTING'] = True
#         self.app = app.test_client()

#     def test_purchasePlaces(self):
#         # DONNÉES FICTIVES POUR LA REQUÊTE POST
#         data = {
#             'competition': 'Spring Festival',
#             'club': 'Iron Temple',
#             'places': '2'
#         }

#         # APPEL DE LA ROUTE PURCHASEPLACES AVEC LES DONNÉES FICTIVES DE TEST
#         response = self.app.post('/purchasePlaces', data=data, follow_redirects=True)

#         # VÉRIFIER SI UN MESSAGE FLASH EST PRÉSENT
#         self.assertIn(b'Error', response.data)

#         # VÉRIFIER SI WELCOME RENVOIE LES BONNES DONNÉES
#         self.assertEqual(response.status_code, 200)

import unittest
from server import app

class TestPurchasePlaces(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_purchasePlaces_invalidNumberOfPlaces(self):
        data = {
            'competition': 'Fall Classic',
            'club': 'Iron Temple',
            'places': '0'  # Nombre de places invalide
        }
        response = self.app.post('/purchasePlaces', data=data, follow_redirects=True)
        self.assertIn(b'Error - Invalid number of places requested!', response.data)  # Vérifie si le message d'erreur est présent dans la réponse
        self.assertEqual(response.status_code, 200)  # Vérifie si la réponse renvoie le code 200 (succès)

    def test_purchasePlaces_competitionOrClubNotFound(self):
        data = {
            'competition': 'Invalid Competition',
            'club': 'Invalid Club',
            'places': '2'
        }
        response = self.app.post('/purchasePlaces', data=data, follow_redirects=True)
        self.assertIn(b'Error - Competition or club not found!', response.data)  # Vérifie si le message d'erreur est présent dans la réponse
        self.assertEqual(response.status_code, 200)  # Vérifie si la réponse renvoie le code 200 (succès)

    def test_purchasePlaces_successfulBooking(self):
        data = {
            'competition': 'Fall Classic',
            'club': 'Iron Temple',
            'places': '2'
        }
        response = self.app.post('/purchasePlaces', data=data, follow_redirects=True)
        self.assertIn(b'Great-booking complete!', response.data)  # Vérifie si le message de succès est présent dans la réponse
        self.assertEqual(response.status_code, 200)  # Vérifie si la réponse renvoie le code 200 (succès)

if __name__ == '__main__':
    unittest.main()

