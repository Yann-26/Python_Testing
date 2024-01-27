import unittest
from flask import flash
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

        # OBTENTION DU NOMBRE DE PLACES AVANT LA RÉSERVATION
        competition_before_booking = next((c for c in competitions if c['name'] == data['competition']), None)
        places_before_booking = int(competition_before_booking['numberOfPlaces'])

        # APPEL DE LA ROUTE PURCHASEPLACES AVEC LES DONNÉES FICTIVES DE TEST
        response = self.app.post('/purchasePlaces', data=data, follow_redirects=True)

        # CLUB ET COMPÉTITION APRÈS L'ACHAT
        club_after_booking = next((c for c in clubs if c['name'] == data['club']), None)
        competition_after_booking = next((c for c in competitions if c['name'] == data['competition']), None)

        # MISE À JOUR DU NOMBRE DE PLACES
        places_after_booking = int(competition_after_booking['numberOfPlaces'])
        self.assertEqual(places_after_booking, places_before_booking - int(data['places']))

        # VÉRIFIER SI UN MESSAGE FLASH EST PRÉSENT
        self.assertIn(b'Great - Booking complete!', response.data)

        # VÉRIFIER SI WELCOME RENVOIE LES BONNES DONNÉES
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
