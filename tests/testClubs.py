import os
import json
import unittest
from server import loadClubs

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

if __name__ == '__main__':
    unittest.main()






