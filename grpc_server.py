import grpc
from concurrent import futures
import weather_pb2
import weather_pb2_grpc
import weather 

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
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    weather_pb2_grpc.add_WeatherServiceServicer_to_server(WeatherServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()