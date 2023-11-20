from flask import Flask, request, render_template
import requests


app = Flask(__name__)
my_api = 'YOUR_API_HERE'

def get_weather(x):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={x}&appid={my_api}'
    response = requests.get(url)
    weather_data = response.json()

    coordinate_lo = weather_data['coord']['lon']
    coordinate_la = weather_data['coord']['lat']
    main_weather = weather_data['weather'][0]['main']
    description = weather_data['weather'][0]['description']
    temp = weather_data['main']['temp']
    temp_min = weather_data['main']['temp_min']
    temp_max = weather_data['main']['temp_max']
    feels_like = weather_data['main']['feels_like']
    pressure = weather_data['main']['pressure']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    wind_deg = weather_data['wind']['deg']

    return coordinate_lo, coordinate_la, main_weather, description, temp, temp_min, temp_max, feels_like, pressure, humidity, wind_speed, wind_deg

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        coordinate_lo, coordinate_la, main_weather, description, temp, temp_min, temp_max, feels_like, pressure, humidity, wind_speed, wind_deg = get_weather(city)
        return render_template('weather.html', city=city,  coordinate_lo=coordinate_lo, coordinate_la=coordinate_la, main_weather=main_weather, description=description, temp=temp, temp_min=temp_min, temp_max=temp_max, feels_like=feels_like, pressure=pressure, humidity=humidity,wind_speed=wind_speed, wind_deg=wind_deg)
    return render_template('index.html')
app.run(debug=True)
