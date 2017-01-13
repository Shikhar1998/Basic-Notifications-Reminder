import urllib
import urllib2
import time
import json
#install using facebook-sdk"
import facebook
def main():
    access = "https://graph.facebook.com/"
    ACCESS_TOKEN = XXXXXXXXXXXXX #enter your access token here
    datafile = urllib2.urlopen(access + 'me?fields=feed&access_token='+ACCESS_TOKEN)
    sigma = 0
    try: 
        fo = open("log.txt","r+")
    except IOError:
        sigma = ""
        fo = open("log.txt","w+")
    n = 0
    #number of new notifications
    #accessing this functionality for first time
    if sigma == "":
            n = "Configuration Successful : Automatic display every 30 minutes ON" 
            index = 0
            for ch in json.loads(datafile.read())["feed"]["data"]:
                if index == 0:
                    fo = open("log.txt","w")
                    fo.write(ch["created_time"][11:19])
                    index = 1
            
    else:
        x = fo.readline()
        so = []
        temp = ""
        for j in x:
            if j!= ":":
                temp += j
            else:
                so.append(temp)
                temp = ""
        so.append(temp)
        temp = ""
        index = 0
        ans = ""
        two = ""
        for ch in json.loads(datafile.read())["feed"]["data"]:
            if index == 0:
                fo = open("log.txt","w")
                ans = ch["message"]
                two = ch["id"]
                k = two.index("_")
                two = two[:k]
                graph = facebook.GraphAPI(ACCESS_TOKEN)
                profile = graph.get_object(two)
                index = 1
            l = []
            t = 0
            sota = []
            for j in ch["created_time"][11:19]:
                if j!= ":" :
                    temp += j
                else:
                    sota.append(temp)
                    temp = ""
            sota.append(temp)
            temp = ""
            if sota[0]<=so[0] and sota[1]<=so[1] and sota[2]<=so[2]:
                break 
            else:
                n = n + 1
    if type(n) == str:
        return n,0,0
    else:
        # returning data : number of new posts, post and the name of the person who posted the data
        return n,ans,profile["name"]            
        

