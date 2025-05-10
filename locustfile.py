from locust import HttpUser, task, between
import uuid

class ChatUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def send_message(self):
        sender_id = str(uuid.uuid4())
        messages = ["Hi", "I want to buy shoes", "What's the price?", "Thank you"]
        for msg in messages:
            self.client.post(
                "/webhooks/rest/webhook",
                json={"sender": sender_id, "message": msg}
            )
