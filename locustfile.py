from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        host = "https://employeemanagementsystem-navi.onrender.com/"
        self.client.get("")
        self.client.get("login/")