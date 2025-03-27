import grpc
from concurrent import futures
import hello_unary_pb2_grpc as pb2_grpc
import hello_unary_pb2 as pb2


class HelloServicer(pb2_grpc.HelloServiceServicer):
    def hello_world(self, request, context):
        response_map = {"greeting": "Hello " + str(request.name)}

        return pb2.Hello(**response_map)


if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_HelloServiceServicer_to_server(HelloServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

