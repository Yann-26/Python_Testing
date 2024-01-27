import unittest
from server import app

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