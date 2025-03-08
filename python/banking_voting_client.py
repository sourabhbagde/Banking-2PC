'''
@author : Sourabh Bagde
'''
import grpc

def run():
    # connecting host to gRPC server at port 50051 as channel
    with grpc.insecure_channel('localhost:50051') as channel:
       # To-Do: have to create stub and pass the stub and parameters to the server.
       # here...
       pass

if __name__ == '__main__':
    run()