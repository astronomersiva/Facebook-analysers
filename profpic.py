from facepy import GraphAPI
import urllib
import os

# Initialize the Graph API with a valid access token  
#Generate access token here: https://developers.facebook.com/tools/explorer/ 
oauth_access_token = 'Access token'  
graph = GraphAPI(oauth_access_token)
membersList = []

#Get the members list. Deactivated and disabled profiles are not returned.
flistPages = graph.get('groupIdHere/members',page = True)
try:
    for flistPage in flistPages:
        for friend in flistPage['data']:
            print friend['id']
            membersList.append(friend['id'])
except:
    pass

count = len(membersList)
print "%d friends have to be processed"%count
os.chdir("c:\\Python27\\facepile")
sCount = 0
fCount = 0
for x in membersList:
    memID = str(x)
    url = "https://graph.facebook.com/" + memID + "/picture"
    saveID = memID + ".jpg"
    try:
        urllib.urlretrieve(url, saveID)
        sCount = sCount + 1
    except:
        fCount = fCount + 1
print "%d processed successfully, %d failed"%(sCount,fCount) 
