"""
Erika Ambrioso
eambrioso2017@my.fit.edu
Launch Tracker

"""
# These are the libraries used by the program.
import json, requests, sys
import ui

print("Welcome to my launch tracker\n")

url = "https://fdo.rocketlaunch.live/json/launches/next/5"

response = requests.get(url)
response.raise_for_status()
data = json.loads(response.text)
d = data['result']
i= 1

for ele in d:
	#print(ele)
	
	print(ele['name'])
	provider = ele['provider']
	print(provider['name'])
	vehicle = ele['vehicle']
	print(vehicle['name'])
	location = ele['pad']
	location = location['location']
	print(location['name'])
	mission = ele['launch_description']
	print(mission)
	
	if ele['weather_summary']:
		print('The weather is predicted to be: ')
		print(ele['weather_summary'])
	
	print('\n')
	
