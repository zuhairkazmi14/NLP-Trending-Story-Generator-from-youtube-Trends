import grpc
import trendstory_pb2
import trendstory_pb2_grpc

def run():
    # Connect to the server
    channel = grpc.insecure_channel('localhost:50051')
    stub = trendstory_pb2_grpc.TrendStoryServiceStub(channel)

    # Create a request with title and theme
    request = trendstory_pb2.TrendRequest(
        title="Artificial Intelligence",
        theme="sci-fi"
    )

    # Make the RPC call
    response = stub.GenerateStory(request)

    # Print the response
    print("Generated Story:\n", response.story)

if __name__ == "__main__":
    run()
