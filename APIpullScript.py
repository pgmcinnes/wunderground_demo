"""
Created on Fri Sep 22 17:35:47 2017

@author: Garrett McInnes

Demo script pulling data utilizing the Weather Underground API

Target City is Philadelphia, PA

"""

#API_key = 20b0a508fdef779b
#project_name='WUnderground API'
from urllib2 import urlopen
import json

weather = urlopen('http://api.wunderground.com/api/20b0a508fdef779b/geolookup/conditions/q/PA/Philadelphia.json')
weather_json = weather.read()
parsed_json = json.loads(weather_json)
city = parsed_json['location']['city']
state = parsed_json['location']['state']
current_temp = parsed_json['current_observation']['temp_f']
feels_like = parsed_json['current_observation']['feelslike_f']
current_conditions = parsed_json['current_observation']['weather']


print('Current temperature in %s, %s: %s deg F' % (city,state, current_temp))
print('It is currently %s in %s, %s.' % (current_conditions,city,state))