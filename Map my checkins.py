from facepy import GraphAPI
from motionless import *
import urllib2

# Initialize the Graph API with a valid access token  
#Generate access token here: https://developers.facebook.com/tools/explorer/
oauth_access_token = 'Enter access token here'  
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
