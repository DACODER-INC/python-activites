import requests

def get_weather(city):
    api_key = "YOUR_API_KEY_HERE"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"Weather in {city}: {temp}°C with {desc}.")
    else:
        print("City not found. Check your spelling!")

get_weather("New York")