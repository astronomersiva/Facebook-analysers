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
friendLocations=[]

#Get friends' locations using FQL.
locations=graph.fql('SELECT uid,current_location FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())')

for location in locations['data']:
    if location['current_location'] is not None:
        if location['current_location']['name'] in friendLocations:
            pass
        else:
            placeMark=location['current_location']['name']
            dmap.add_marker(AddressMarker(placeMark,label=''))
            friendLocations.append(placeMark)
            print placeMark
            #Static Map URLs can only be of 2048 characters or less. 
            try:
                mapurl = dmap.generate_url()
            except:
                break


print mapurl

#Post the map to Facebook
graph.post(path = 'me/photos', source = urllib2.urlopen(mapurl), message="Here is a map of all my friends. Can you find yourself?" )
