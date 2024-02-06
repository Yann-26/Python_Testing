import unittest
import os
from server import app
from server import loadClubs, loadCompetitions, competitions, clubs



class TestBookingRoute(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_booking(self):
        response = self.app.get('/book/Fall%20Classic/Iron%20Temple')
        self.assertEqual(response.status_code, 200)
        
class TestLoadClubs(unittest.TestCase):
    def test_loadClubs(self):
        # Créez un fichier JSON de test avec des données fictives pour les clubs
        test_json_data = '{"clubs": ["Club A", "Club B", "Club C"]}' 
        with open('test_clubs.json', 'w') as test_file:
            test_file.write(test_json_data)
        # Appel de la fonction loadClubs pour charger les clubs à partir du fichier de test
        loaded_clubs = loadClubs('test_clubs.json')
        # Vérifiez si les clubs ont été chargés correctement
        self.assertEqual(loaded_clubs, ["Club A", "Club B", "Club C"])
        os.remove('test_clubs.json')

class TestLoadClubs(unittest.TestCase):
    def test_loadClubs(self):
        # Créez un fichier JSON de test avec des données fictives pour les clubs
        test_json_data = '{"clubs": ["Club A", "Club B", "Club C"]}' 
        with open('test_clubs.json', 'w') as test_file:
            test_file.write(test_json_data)
        # Appel de la fonction loadClubs pour charger les clubs à partir du fichier de test
        loaded_clubs = loadClubs('test_clubs.json')
        # Vérifiez si les clubs ont été chargés correctement
        self.assertEqual(loaded_clubs, ["Club A", "Club B", "Club C"])
        os.remove('test_clubs.json')

class TestloadCompetitions(unittest.TestCase):
    def test_loadCompetitions(self):
        test_json_data = '{"competitions": ["Competition A", "Competition B"]}'
        with open('test_competitions.json', 'w') as test_file:
            test_file.write(test_json_data)
        chargComp = loadCompetitions('test_competitions.json')
        self.assertEqual(chargComp, ["Competition A", "Competition B"])
        os.remove('test_competitions.json')

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

class TestShowSummary(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client() # CONFIGURATION DU SERVER DE TEST

    def test_showSummary(self):
       
        data = {'email': 'admin@irontemple.com'} 
        response = self.app.post('/showSummary', data=data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()