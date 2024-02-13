import unittest
from flask import url_for
from server import app

class TestLogout(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_logout(self):
        with app.test_request_context():
            response = self.app.get('/logout')
            self.assertEqual(response.status_code, 302) 
            # self.assertEqual(response.location, 'http://localhost/')  # Vérifie si la redirection est effectuée vers la page d'accueil

if __name__ == '__main__':
    unittest.main()
