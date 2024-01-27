import unittest
from server import app

class TestBookingRoute(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_booking(self):
        response = self.app.get('/book/Fall%20Classic/Iron%20Temple')
        self.assertEqual(response.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()