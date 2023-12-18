import os
from flask import Flask, render_template, request, Blueprint
import requests

weatherapp_app = Blueprint("weatherapp",__name__)

def get_weather(api_key, city, country):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': f'{city},{country}',
        'appid': api_key,
        'units': 'metric'  # You can use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            return f'Temperature in {city}, {country}: {temperature}°C\nWeather Description: {description}'
        else:
            return f'Error: {data["message"]}'

    except Exception as e:
        return f'An error occurred: {e}'

@weatherapp_app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        api_key = os.environ.get("weather")
        city = request.form['city']
        country = request.form['country']
        weather_info = get_weather(api_key, city, country)
        return render_template('weatherapp.html', weather_info=weather_info)
    return render_template('weatherapp.html')

