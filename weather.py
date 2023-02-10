import requests
import os
from datetime import datetime

location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid=6c4664c499bab98f55c36af7b4589bc7"

#backup api keys 6c4664c499bab98f55c36af7b4589bc7
#backup api keys 9dbe620050fc33de74dda9fa220676a3

api_link = requests.get(complete_api_link)
api_data = api_link.json()
# print(api_data)

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is      : {:.2f} Degree Celsius".format(temp_city))
print ("Current weather description :",weather_desc)
print ("Current Humidity            :",hmdt, '%')
print ("Current wind speed          :",wind_spd ,'Kmph')
