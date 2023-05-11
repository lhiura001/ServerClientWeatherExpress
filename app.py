from flask import Flask, request, jsonify
import weather

app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return 'Welcome to the Weather API'

# Weather route
@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    unit = request.args.get('unit')
    response = weather.get_response(city)
    if response is not None:
        weather_summary = weather.get_weather_summary(response, unit)
        temperatures = weather.get_temperatures(response, unit)
        humidity = weather.get_humidity(response)
        print(weather_summary)
        print(temperatures)
        print(humidity)
        return jsonify({
            'weather_summary': weather_summary[1],
            'weather_description': weather_summary[0],
            'high_temp_pm': temperatures[0],
            'high_temp_am': temperatures[1],
            'high_temp_night': temperatures[2],
            'low_temp_pm': temperatures[3],
            'low_temp_am': temperatures[4],
            'low_temp_night': temperatures[5],
            'humidity_pm': humidity[0],
            'humidity_am': humidity[1],
            'humidity_night': humidity[2]
        })
    else:
        return jsonify({'error': 'Invalid city name'})

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=8082, debug=True)
