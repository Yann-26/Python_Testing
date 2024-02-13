from datetime import datetime
import json
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


class TestloadCompetitions(unittest.TestCase):
    def test_loadCompetitions(self):
        with open('competitions.json') as f:
            data = json.load(f)
        current_date = datetime.now()
        competitions = [competition for competition in data.get('competitions', []) if datetime.strptime(competition["date"], "%Y-%m-%d %H:%M:%S") >= current_date]
        chargComp = loadCompetitions('competitions.json')
        self.assertEqual(chargComp, competitions)

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