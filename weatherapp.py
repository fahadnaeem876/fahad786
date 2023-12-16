import os
from flask import Flask, render_template, request, Blueprint
import requests

weatherapp_app = Blueprint("weatherapp",__name__)

def get_weather(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    print("API Response:", data)

    if data["cod"] != "404":
        main_data = data["main"]
        weather_data = data["weather"][0]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        description = weather_data["description"]
        return {
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "description": description
        }
    else:
        return None

@weatherapp_app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get("city")
        api_key = os.environ.get("weather")
        weather_data = get_weather(api_key, city)
        if weather_data:
            return render_template("weatherapp.html", weather_data=weather_data)
        else:
            return render_template("weatherapp.html", error="City not found!")

    return render_template("weatherapp.html", weather_data=None, error=None)
