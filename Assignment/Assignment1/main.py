# import necesarry modules from libary
import json
import urllib.request
import turtle
import time

# initial variable to hold api request url
apiUrl = 'http://api.open-notify.org/astros.json'
# make a variable to hold resposne of request
response = urllib.request.urlopen(apiUrl)
# make a varibale to store the data within the response
data = json.loads(response.read())
# print data for test
# print(data)
# print the number of peopel within the space station
print("People in the space station:", data['number'])
# loop through the data and print the name
for person in data['people']:
    print(person['name'], 'in', person['craft'])


# send request to get location data
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
data = json.loads(response.read())
# make a variable to store the location of the space station
location = data['iss_position']
# initial two variables to store longitude and latitude
latitude = float(location['latitude'])
longitude = float(location['longitude'])
# print out latitude and longitude
print("Latitude is:", latitude, 'and', "Latitude is:", longitude)


# configure screen, set up map
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('./image/map.gif')
screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('./image/map.gif')
screen.register_shape('./image/iss.gif')

iss = turtle.Turtle()
iss.shape('./image/iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(longitude, latitude)

# potion of space center, Houston
latitudeHous = 29.5502
longitudeHous = -95.097
# mark the location of space center on the map
location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(longitudeHous, latitudeHous)
location.dot(5)
location.hideturtle()

# get the time that when spece station is going to move to the location of space center
url = 'http://api.open-notify.org/iss-pass.json?lat=' + \
    str(latitudeHous) + '&lon=' + str(longitudeHous)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

# print result
over = result['response'][1]['risetime']
location.write(time.ctime(over))
turtle.mainloop()
