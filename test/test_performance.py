from locust import HttpUser, task, between
import json
import random

class TestPerformance(HttpUser):
    wait_time = between(1, 2)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.competitions = self.load_data('competitions.json')['competitions']
        self.clubs = self.load_data('clubs.json')['clubs']

    def load_data(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    @task
    def index(self):
        try:
            if self.competitions and self.clubs:
                competition = random.choice(self.competitions)
                club = random.choice(self.clubs)

                self.client.post('/showSummary', data={'email': club['email']})
                self.client.get(f'/book/{competition["name"]}/{club["name"]}')
                self.client.post('/purchasePlaces', data={'competition': competition['name'], 'club': club['name'], 'places': '2'})
            else:
                print("No competitions or clubs available.")
        except Exception as e:
            self.environment.events.request_failure.fire(
                request_type="http",
                name="index",
                response_time=0,
                exception=e
            )

