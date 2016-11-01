#this Python 3 module accepts inputs and returns the temperature in a city in degrees celcius using the Openweathermap API
#it must be executed from the commandline using an interpreter
import requests

def tempname(city):
	b = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=1c84997bbd99db105f632758fd942d90') #this will accept the city name and search using it
	json_2 = b.json()
	temp_k = float(json_2["main"]["temp"])
	temp_c = temp_k - 273.15
	print("The temperature of", city,"in degrees Celcius is", int(temp_c))
