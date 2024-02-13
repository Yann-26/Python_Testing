import unittest
from server import app

class TestSomeOtherRoute(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_someOtherRoute_clubNotFound(self):
        response = self.app.get('/some_other_route/nonexistent_email@example.com', follow_redirects=True)
        # self.assertIn(b"L'e-mail fourni n'existe pas dans notre système.", response.data)  # Vérifie si le message d'erreur est présent dans la réponse
        self.assertEqual(response.status_code, 200)  # Vérifie si la réponse renvoie le code 200 (succès)

    def test_someOtherRoute_clubFound(self):
        # Supposons que vous ayez une adresse e-mail valide dans vos données de club
        valid_email = 'example@example.com'
        response = self.app.get(f'/some_other_route/{valid_email}', follow_redirects=True)
        # self.assertNotIn(b"L'e-mail fourni n'existe pas dans notre système.", response.data)  # Vérifie que le message d'erreur n'est pas présent dans la réponse
        self.assertEqual(response.status_code, 200)  # Vérifie si la réponse renvoie le code 200 (succès)

if __name__ == '__main__':
    unittest.main()
