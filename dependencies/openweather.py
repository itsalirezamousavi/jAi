import requests, json                                                                   # importing libs

def upcomingWeather(city_name):                                                         # weather func
    api_key = "" #Put Your API Key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name                    # creating url
    try:
        response = requests.get(complete_url)                                           # trying to access api
    except:
        return 'Api is Unavailable right now'
    x = response.json()

    if x["cod"] != "404":                                                               # getting data
        weather_description = x['weather'][0]["description"]
        return weather_description
    else:
        return 'City Not Found'

#print(upcomingWeather('london'))