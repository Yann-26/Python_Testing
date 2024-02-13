import os
import json
import unittest
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for
from server import app, loadClubs, loadCompetitions

# Importation de la fonction pour ajouter un ticket
from ajout_ticket import ajouter_ticket

# Définition du chemin des fichiers de données
clubs_file = 'clubs.json'
competitions_file = 'competitions.json'

# Configuration de l'application Flask pour les tests
app.config['TESTING'] = True
app.secret_key = 'something_special'

# Chargement des données des clubs et des compétitions
clubs = loadClubs(clubs_file)
competitions = loadCompetitions(competitions_file)

class TestBookingRoute(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_booking(self):
        response = self.client.get('/book/Fall%20Classic/Iron%20Temple')
        self.assertEqual(response.status_code, 200)

class TestLoadClubs(unittest.TestCase):
    def test_loadClubs(self):
        # Création d'un fichier JSON de test avec des données fictives pour les clubs
        test_clubs_data = {'clubs': ["Club A", "Club B", "Club C"]}
        with open('test_clubs.json', 'w') as test_file:
            json.dump(test_clubs_data, test_file)
        
        # Chargement des clubs à partir du fichier de test
        loaded_clubs = loadClubs('test_clubs.json')
        
        # Vérification si les clubs ont été chargés correctement
        self.assertEqual(loaded_clubs, test_clubs_data['clubs'])

        # Nettoyage du fichier de test créé
        os.remove('test_clubs.json')

class TestLoadCompetitions(unittest.TestCase):
    def test_loadCompetitions(self):
        # Création d'un fichier JSON de test avec des données fictives pour les compétitions
        test_competitions_data = {'competitions': [
            {"name": "Competition A", "date": "2025-03-27 10:00:00", "numberOfPlaces": "25"},
            {"name": "Competition B", "date": "2025-10-22 13:30:00", "numberOfPlaces": "13"}
        ]}
        with open('test_competitions.json', 'w') as test_file:
            json.dump(test_competitions_data, test_file)
        
        # Chargement des compétitions à partir du fichier de test
        loaded_competitions = loadCompetitions('test_competitions.json')
        
        # Vérification si les compétitions ont été chargées correctement
        self.assertEqual(loaded_competitions, test_competitions_data['competitions'])

        # Nettoyage du fichier de test créé
        os.remove('test_competitions.json')


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


class TestShowSummary(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_showSummary(self):
        data = {'email': 'admin@irontemple.com'} 
        response = self.client.post('/showSummary', data=data)
        self.assertEqual(response.status_code, 200)

class TestLogoutFunction(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_logout_redirect(self):
        # Effectuer une requête GET vers la route /logout
        response = self.client.get('/logout', follow_redirects=True)
        
        # Vérifier si la redirection vers la page d'accueil a eu lieu
        self.assertEqual(response.status_code, 200)  # Code de statut 200 indique succès

class TestIndexRoute(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # Vérifie si la réponse renvoie le code 200 (succès)

if __name__ == '__main__':
    unittest.main()
