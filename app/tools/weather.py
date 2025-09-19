import requests
import os

WEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

def get_weather(city):
    """Obtener información del clima para una ciudad"""

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&Lang=es"
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            return f"El clima en {city}: {description}, temperatura: {temp}°C"
        else:
            return f"Error al obtener el clima: {data.get('message', 'Ciudad no encontrada')}"
            
    except Exception as e:
        return f"Error al obtener el clima {str(e)}"
