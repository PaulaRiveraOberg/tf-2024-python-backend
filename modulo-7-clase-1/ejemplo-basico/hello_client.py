import grpc
import hello_unary_pb2_grpc as pb2_grpc
import hello_unary_pb2 as pb2
from google.protobuf.json_format import MessageToJson

if __name__ == "__main__":
    with (grpc.insecure_channel("localhost:50051") as channel):
        stub = pb2_grpc.HelloServiceStub(channel)

        message = pb2.User(name="Talento Futuro")

        print(f"Message sent:\n{MessageToJson(message)}\n")

        # call remote method
        response = stub.hello_world(message)

        print(f"Message received:\n{MessageToJson(response)}\n")
