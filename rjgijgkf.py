try:
    import requests  # type: ignore
    _HAS_REQUESTS = True
except ImportError:
    # Fallback to urllib if requests is not installed
    import urllib.request, urllib.parse, json
    _HAS_REQUESTS = False

def get_weather(city):
    api_key = "YOUR_API_KEY_HERE"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    if _HAS_REQUESTS:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
        else:
            print("City not found. Check your spelling!")
            return
    else:
        # use urllib as fallback
        try:
            with urllib.request.urlopen(url) as resp:
                if resp.status == 200:
                    data = json.loads(resp.read().decode())
                else:
                    print("City not found. Check your spelling!")
                    return
        except Exception:
            print("Network error or city not found.")
            return
    # if we reach here, data should be available
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f"Weather in {city}: {temp}°C with {desc}.")

get_weather("New York")