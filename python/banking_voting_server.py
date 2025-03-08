'''
@authors : Sourabh Bagde
'''
import grpc
from concurrent import futures
import logging

def serve():
    # port is defined and assigned to value of server port running at 50051.
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # To-Do: have to bind the gRPC service class to server, to handle incoming messages.
    # here...
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Banking Service gRPC server started and is runnning on port " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
