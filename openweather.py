#! python3
# openweather.py
# Created by Lori Imbesi 2021.02

# This program will display the temperature for a particular zip code in the US.

import requests
import configparser
import json
import re
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather_report', methods=['POST'])
def render_weather_report():
    zip_code = request.form['zipCode']

    api_key = get_api_key()
    data = get_weather_results(zip_code, api_key)
    temp = "{0:.1f}".format(data["main"]["temp"])
    feels_like = "{0:.1f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]

    return render_template('weather_report.html', location=location,
                           temp=temp, feels_like=feels_like, weather=weather)


def get_weather_results(zip_code, api_key):
    api_url = 'http://api.openweathermap.org/data/2.5/weather?zip={}&units=imperial&appid={}'.format(
        zip_code, api_key)
    r = requests.get(api_url)
    return r.json()


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


if __name__ == "__main__":
    app.run(debug=True)
