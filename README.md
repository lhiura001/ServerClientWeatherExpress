# WeatherExpress

WeatherExpress is a microservice application that provides weather data for different cities around the world. This README outlines the communication contract for the Weather microservice, which allows developers to retrieve weather data programmatically.

# Using the Weather Microservice with gRPC

To use the Weather microservice in your client code, you will need to download the protobuf files provided in the serverclient zip folder and add them to your project directory. These files define the data structures and RPC methods used by the Weather service and are required to generate client and server code in the programming language of your choice.

## What is gRPC?

gRPC is a modern, high-performance framework that enables efficient communication between distributed systems. It uses Protocol Buffers, a language-agnostic binary serialization format, to define the structure of the data being exchanged and generates client and server code in multiple programming languages. The resulting code is type-safe, easy to use, and highly performant, making it ideal for building microservices and other distributed systems.

## How gRPC Works

To use gRPC in your project, you first define the data structures and RPC methods using Protocol Buffers, and then use the gRPC toolchain to generate client and server code in your chosen programming language. You can then use this generated code to communicate with your gRPC server and exchange data.

The gRPC framework handles many of the low-level details of network communication, such as establishing connections, sending data, and handling errors. It also provides built-in support for advanced features like authentication, load balancing, and distributed tracing, making it a powerful tool for building complex distributed systems.

## Using gRPC with the Weather Microservice

In the case of the Weather microservice, the protobuf files define the WeatherRequest and WeatherResponse message types, as well as the GetWeather RPC method that allows clients to request weather data for a specific city. By importing these files into your client code and using the generated gRPC client code, you can easily request weather data from the Weather microservice and use it in your application.

Using gRPC to communicate with the Weather microservice offers several advantages over other communication methods, such as REST or SOAP. For example, gRPC is more efficient than REST because it uses binary serialization rather than text-based formats like JSON or XML. This makes it faster and more compact, resulting in lower network usage and higher performance. Additionally, gRPC's built-in support for streaming allows you to easily receive continuous updates from the Weather service, making it ideal for real-time applications.

## Communication Contract

The Weather microservice uses gRPC as its main communication pipeline. To request weather data from the microservice, follow these instructions:

### Requesting Data



1. Create a gRPC channel to connect to the Weather microservice.

    ```python
    channel = grpc.insecure_channel('localhost:50051')
    ```

2. Create a stub object for the Weather service.

    ```python
    stub = weather_pb2_grpc.WeatherServiceStub(channel)
    ```

3. Create a request object with the city name and unit.

    ```python
    request = weather_pb2.WeatherRequest(city=city, unit=unit)
    ```

4. Call the `GetWeather` method on the Weather service stub, passing in the request object.

    ```python
    response = stub.GetWeather(request)
    ```

5. Convert the response to a JSON object.

    ```python
    json_response = {
        'weather_summary': response.weather_summary,
        'weather_description':response.weather_description, 
        'high_temp_pm': response.high_temp_pm,
        'high_temp_am': response.high_temp_am,
        'high_temp_night': response.high_temp_night,
        'low_temp_pm': response.low_temp_pm,
        'low_temp_am': response.low_temp_am,
        'low_temp_night': response.low_temp_night,
        'humidity_pm': response.humidity_pm,
        'humidity_am': response.humidity_am,
        'humidity_night': response.humidity_night
    }
    ```

6. Return the JSON response.

    ```python
    return json.dumps(json_response)
    ```

Here's an example call to retrieve the weather data for New York City in Celsius:

```python
import grpc
import weather_pb2
import weather_pb2_grpc
import json

channel = grpc.insecure_channel('localhost:50051')
stub = weather_pb2_grpc.WeatherServiceStub(channel)

request = weather_pb2.WeatherRequest(city='New York', unit='c')
response = stub.GetWeather(request)

json_response = {
    'weather_summary': response.weather_summary,
    'weather_description':response.weather_description, 
    'high_temp_pm': response.high_temp_pm,
    'high_temp_am': response.high_temp_am,
    'high_temp_night': response.high_temp_night,
    'low_temp_pm': response.low_temp_pm,
    'low_temp_am': response.low_temp_am,
    'low_temp_night': response.low_temp_night,
    'humidity_pm': response.humidity_pm,
    'humidity_am': response.humidity_am,
    'humidity_night': response.humidity_night
}

print(json_response)
```





