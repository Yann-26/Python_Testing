import os
import json
import unittest
from datetime import datetime
from server import loadCompetitions

class TestloadCompetitions(unittest.TestCase):
    def test_loadCompetitions(self):
        with open('competitions.json') as f:
            data = json.load(f)
        current_date = datetime.now()
        competitions = [competition for competition in data.get('competitions', []) if datetime.strptime(competition["date"], "%Y-%m-%d %H:%M:%S") >= current_date]
        chargComp = loadCompetitions('competitions.json')
        self.assertEqual(chargComp, competitions)