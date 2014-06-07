#Division in Python returns integers. To get floating point values, we import division from __future__
from __future__ import division
from facepy import GraphAPI

# Initialize the Graph API with a valid access token  
#Generate access token here: https://developers.facebook.com/tools/explorer/ 
oauth_access_token = 'Enter access token here'  
graph = GraphAPI(oauth_access_token)

#initialize the variables
maleCount = 0
femaleCount = 0

#Get the friend list. Deactivated and disabled profiles are not returned.
flist=graph.get('me/friends?fields=gender')

#Get the number of friends by finding the length of flist. 
count=len(flist['data'])

#Iterate over individual profiles. 
for friend in flist['data']:
    #Checks whether the friend has his gender set to visible.
    if friend.has_key('gender'):
        friendGender = friend['gender']
        if friendGender=='male':
            maleCount+=1
        else:
            femaleCount+=1

#Calculate the percentages.
malePercentage = (maleCount/count)*100
femalePercentage = (femaleCount/count)*100

print "You have %s friends\n%s are male and %s are female"%(count,maleCount,femaleCount)
print "Male percentage:%.1f\nFemale percentage:%.1f"%(malePercentage,femalePercentage)
fbStatus="I have %s friends\n%s are male and %s are female"%(count,maleCount,femaleCount)+\
      "\nMale percentage:%.1f\nFemale percentage:%.1f"%(malePercentage,femalePercentage)

#Posts to facebook
graph.post('me/feed',message=fbStatus)

