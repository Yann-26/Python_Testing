import os
import json
import unittest
from server import  loadCompetitions


class TestloadCompetitions(unittest.TestCase):
    def test_loadCompetitions(self):
        test_json_data = '{"competitions": ["Competition A", "Competition B"]}'
        with open('test_competitions.json', 'w') as test_file:
            test_file.write(test_json_data)
        chargComp = loadCompetitions('test_competitions.json')
        self.assertEqual(chargComp, ["Competition A", "Competition B"])
        os.remove('test_competitions.json')

if __name__ == '__main__':
    unittest.main()