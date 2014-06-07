from facepy import *

#Create a dictionary to save the number of friends born in each month
bdayMonths={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}

#Create another dictionary to display month names
monthText={1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}

# Initialize the Graph API with a valid access token  
#Generate access token here: https://developers.facebook.com/tools/explorer/
oauth_access_token = 'Enter access token here'  
graph = GraphAPI(oauth_access_token)

#Get a list of birthdays using Graph API
blist=graph.get('me/friends?fields=birthday')

status="Number of friends born in each month\n"

#Iterate over each birthday
for bday in blist['data']:
    if bday.has_key('birthday'):
        birthday=bday['birthday'].split('/')
        bdayMonth=int(birthday[0])
        bdayMonths[bdayMonth]+=1

#Generate the post
for x in bdayMonths:
    status+=monthText[x]+":"+str(bdayMonths[x])+"\n"

#Post to Facebook
graph.post(path='me/feed',message=status)
    
