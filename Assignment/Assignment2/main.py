# Assignment2 QingbeiHuang
# import modules
from requests import get
import matplotlib.pyplot as plt
from dateutil import parser
# define request url
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallmeasurements/490722'

# define pages variable, initialize as 1
pages = 1
# grab weather data
weather = get(url).json()
weather_data = weather['items']

# get data from 2-9 page
while 'next' in weather and pages < 9:
    url = weather['next']['$ref']
    print('Fetching {0}'.format(url))
    weather = get(url).json()
    weather_data += weather['items']
    pages += 1
# define list of termprature data
list_temp = [record['ambient_temp'] for record in weather_data]
# list_ground_temp = [record['ground_temp'] for record in weather_data]
list_humidity = [record['humidity'] for record in weather_data]
# define a list to store time stamps of termprature data
list_time_stamps = [parser.parse(record['reading_timestamp'])
                    for record in weather_data]

# # use all data to draw graphic 
plt.plot(list_time_stamps, list_temp)
# plt.plot(list_time_stamps, list_ground_temp )
plt.plot(list_time_stamps, list_humidity )
# Set the axis labels
plt.ylabel('Temperature,Ground Temperature,Humidity')
# plt.ylabel('Ground Temperature')
# plt.ylabel('Humidity')
plt.xlabel('Time')
plt.show()

