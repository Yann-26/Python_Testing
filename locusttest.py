from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)
    
    def on_start(self):
        self.client.post("/server.py", {
            "email": "admin@irontemple.com",
            
        })
    
    
    @task
    def about(self):
        self.client.get("Python_Testing/templates/")