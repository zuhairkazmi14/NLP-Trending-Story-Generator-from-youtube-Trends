# locustfile.py
from locust import User, task, between
import grpc
import trendstory_pb2
import trendstory_pb2_grpc
import random

titles = [
    "Trending Title A", "Trending Title B", "Trending Title C"
]  # You can dynamically pull these if needed

titles = ["Papa Papa Main Kahan per baitha hun", "Aaj ka hogaya #abrazkhan  #shorts", "Madni did a devious magic trick for his friend 😂😂"]  # Add your trending titles here

class GrpcClient:
    def __init__(self):
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = trendstory_pb2_grpc.TrendStoryServiceStub(self.channel)

    def generate_story(self, title, theme):
        request = trendstory_pb2.TrendRequest(title=title, theme=theme)
        return self.stub.GenerateStory(request)

class GrpcUser(User):
    wait_time = between(1, 2)

    def on_start(self):
        self.client = GrpcClient()

    @task
    def generate_story_task(self):
        title = random.choice(titles)
        theme = random.choice(themes)
        try:
            response = self.client.generate_story(title, theme)
        except grpc.RpcError as e:
            print(f"gRPC Error: {e}")
