import requests

def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        return {
            'city': city,
            'temp': main['temp'],
            'feels_like': main['feels_like'],
            'weather_condition': weather['main'],
            'dt': data['dt'],
        }
    else:
        print(f"Error fetching data for {city}: {response.status_code}")
        return None
