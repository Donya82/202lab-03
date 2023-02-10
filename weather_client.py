import requests
from typing import Dict

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "c5e3cfb9d53f9503107ee4b822f9212b"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)

URL2 = "https://official-joke-api.appspot.com/random_joke"

def random_joke() -> Dict:
    res2 = requests.get(URL, params={})
    return res.json()
    
def main():
    temp = get_weather("London")
    print(temp)
    temp = random_joke()
    print(temp)

if __name__ == "__main__":
    main()
