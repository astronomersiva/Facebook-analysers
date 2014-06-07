from facepy import GraphAPI
from motionless import *
import urllib2

# Initialize the Graph API with a valid access token  
#Generate access token here: https://developers.facebook.com/tools/explorer/
oauth_access_token = 'CAACEdEose0cBAMapOeoibIOL53zv5wfK6juT4amcPFPv5OkKHr6AwlV9qfSYIkH1c3aTnz23lJ71VAVNhbqfH09ZCOpOV8ODbkTmWTiKKx3z6x12N4t1K86XLtiMPWTbWkxHFkd1DEep1HU3mGW6DbdSv47gqkFX94vHebsvISoCdfC58iC5v0YPphZCJb0BSiN2rZBAgZDZD'  
graph = GraphAPI(oauth_access_token)

#Initialise the output map
dmap = DecoratedMap()

#Initialise a list for the locations.
myLocations=[]

locationResults=graph.get('me/locations',page=True)
for locationResult in locationResults:
    locations = locationResult['data']
    for location in locations:
        try:
            place = location['place']['location']['city']
            #Check whether the place is already in the list. If yes, ignore and continue.
            if place in myLocations:
                pass
            else:
                print place
                myLocations.append(place)
                dmap.add_marker(AddressMarker(place,label=''))
        except:
            pass

#Generate the URL of the static map
mapurl = dmap.generate_url()

print mapurl

#Post the map to Facebook
graph.post(path = 'me/photos', source = urllib2.urlopen(mapurl), message="Here is a map of all my recent check-ins" )
