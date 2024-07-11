# weather.py

import requests # type: ignore

def fetch_weather(city):
    # Replace 'your_api_key' with your actual WeatherAPI key
    api_key = 'd4b662404ad64f9b8e9210841240607'
    url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        current_weather = data['current']
        
        temperature = current_weather['temp_c']
        weather_description = current_weather['condition']['text']
        
        print(f"Current temperature in {city}: {temperature}°C")
        print(f"Weather description: {weather_description}")
    else:
        print("Failed to retrieve weather data. Please check the city name and API key.")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    fetch_weather(city)
