import grpc
import pandas as pd
from concurrent import futures
import weather_pb2
import weather_pb2_grpc
import weather 

# Import the gRPC-Gateway package
from http import server as http_server
from grpc import server as grpc_server
from grpc_health.v1 import health_pb2, health_pb2_grpc
from google.protobuf.json_format import MessageToJson
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc


class WeatherServicer(weather_pb2_grpc.WeatherServiceServicer):

    def GetWeather(self, request, context):
        city = request.city
        unit = request.unit
        response = weather.get_response(city)
        weather_summary = weather.get_weather_summary(response, unit)
        temperatures = weather.get_temperatures(response, unit)
        humidity = weather.get_humidity(response)

        # create a WeatherResponse message and return it
        return weather_pb2.WeatherResponse(
            weather_summary=weather_summary[1],
            weather_description=weather_summary[0],
            high_temp_pm=temperatures[0],
            high_temp_am=temperatures[1],
            high_temp_night=temperatures[2],
            low_temp_pm=temperatures[3],
            low_temp_am=temperatures[4],
            low_temp_night=temperatures[5],
            humidity_pm=humidity[0],
            humidity_am=humidity[1],
            humidity_night=humidity[2]
        )

def serve():
    # Create the gRPC server
    server = grpc_server(futures.ThreadPoolExecutor(max_workers=10))
    weather_pb2_grpc.add_WeatherServiceServicer_to_server(WeatherServicer(), server)
    server.add_insecure_port('[::]:50051')
    
    # Start the gRPC server
    server.start()
    
    # Create the gRPC health check service
    health_servicer = health_pb2_grpc.HealthServicer()
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)

    # Start the gRPC-Gateway server
    gateway_port = 8081
    HOST = 'localhost'
    PORT = 8081
    gateway_server = http_server.HTTPServer((HOST, PORT), http_server.SimpleHTTPRequestHandler)
    gateway_server.serve_forever()

    # Print the gRPC-Gateway URL
    print("gRPC-Gateway listening on http://{}:{}/".format(HOST, gateway_port))

    # Wait for the gRPC server to terminate
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
