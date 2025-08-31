import requests
import json 
import math
city_input = input('Enter city: ')
API_KEY = ''

def kelv_cels(cels):
    return math.floor(cels - 273.15)

if city_input.replace(' ',"").isalpha():
    try:
        city = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_input}&appid={API_KEY}')
        city_data = json.loads(city.text)
        for val in city_data:
            weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={val['lat']}&lon={val['lon']}&appid={API_KEY}')
            weather_data = json.loads(weather.text)
            with open('weather.json','w') as weather_file:
                weather_file.write(json.dumps(weather_data,indent=4))
        
        with open('weather.json') as data:
            d = json.load(data)
            temp = d['main']['temp']
            humidity = d['main']['humidity']
            print(f'temperature in {city_input}: {kelv_cels(temp)} celsius\nhumidity:{math.floor(humidity)}')
    except:
        print('connection failed. code: ',city.status_code)
else:
    print('invalid city name')




