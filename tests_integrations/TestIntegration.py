import unittest
from server import app
from bs4 import BeautifulSoup

class TestIntegration(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_integration(self):
        # Test de la route '/showSummary'
        response = self.client.post('/showSummary', data={'email': 'john@simplylift.co'})
        self.assertEqual(response.status_code, 200)

        # Analyse du contenu HTML avec BeautifulSoup
        soup = BeautifulSoup(response.data, 'html.parser')
        welcome_message = soup.find('h2')

        # Assertions avec BeautifulSoup
        self.assertIsNotNone(welcome_message)
        self.assertIn('Welcome', welcome_message.text)
        self.assertIn('Welcome, john@simplylift.co', welcome_message.text)

        # Test de la route '/book'
        response = self.client.get('/book/SpringFestival/IronTemple')
        self.assertEqual(response.status_code, 200)

        # Analyse du contenu HTML avec BeautifulSoup
        soup = BeautifulSoup(response.data, 'html.parser')
        booking_info = soup.find('div', {'class': 'booking-info'})
        if booking_info:
            # Effectuer des assertions sur l'élément booking_info
            self.assertIn('Booking for Spring Festival at Iron Temple', booking_info.text)
            self.assertIn('Available Places: 100', booking_info.text)
        else:
            return None

        # Assertions avec BeautifulSoup
        self.assertIsNotNone(booking_info)
        self.assertIn('Booking for Spring Festival at Iron Temple', booking_info.text)
        self.assertIn('Available Places: 100', booking_info.text)

        # Test de la route '/purchasePlaces'
        response = self.client.post('/purchasePlaces', data={'competition': 'SpringFestival', 'club': 'IronTemple', 'places': '2'})
        self.assertEqual(response.status_code, 200)

        # Analyse du contenu HTML avec BeautifulSoup
        soup = BeautifulSoup(response.data, 'html.parser')
        flash_message = soup.find('div', {'class': 'flash-message'})

        # Assertions avec BeautifulSoup
        self.assertIsNotNone(flash_message)
        self.assertIn('Great - Booking complete!', flash_message.text)


if __name__ == '__main__':
    unittest.main()
