# trendstory_server.py
import grpc
from concurrent import futures
import trendstory_pb2
import trendstory_pb2_grpc
from transformers import pipeline
import time

class TrendStoryServicer(trendstory_pb2_grpc.TrendStoryServiceServicer):
    def __init__(self):
        self.generator = pipeline("text-generation", model="isarth/distill_gpt2_story_generator")

    def GenerateStory(self, request, context):
        prompt = (
            f"Write a {request.theme}-themed short story inspired by the trending topic:'{request.title}'."
            f"Make the story imaginative and vivid, with a clear beginning, middle, and end. Use humor, irony, or emotion depending on the theme. Add characters, conflicts, and a twist if possible."
        )
        try:
            story = self.generator(prompt, max_length=500, num_return_sequences=1)[0]['generated_text']
            return trendstory_pb2.TrendResponse(story=story)
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return trendstory_pb2.TrendResponse(story="Error generating story")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    trendstory_pb2_grpc.add_TrendStoryServiceServicer_to_server(TrendStoryServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Server running on port 50051...")
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
