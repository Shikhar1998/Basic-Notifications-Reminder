##DOCUMENTATION

###FACEBOOK NOTIFIER  

####PROJECT OVERVIEW: 
The Facebook Notifier is a real-ime Facebook Notifications Display . The project uses the Facebook Graph API inorder to fetch data from your Facebook page and notifies you if there are any new notifications .

###INSTALLATION GUIDE : 

####1. Requirements : 
	a. Facebook ID
	
	b. Facebook App with permission to extract feed data
	
	c. Valid Access Token
	
	d. Arduino UNO
	
	e. BreadBoard
	
	f. LCD Display(16X2)
	
	g. Jumper Wires
	
	h. Python 2.7 or higher
	
	i. An Internet Connection
	
	j. 10K Potentiometer
	
	k. Pin Headers
	
####2. Installation : 
Please follow the steps below:

####1. Installing the package : 
Enter the following commands in the terminal(Linux Users)/cmd(Windows Users) :

`git clone https://github.com/Shikhar1998/Basic-Facebook-Notifications-Reminder.git `

This will clone the repository from github create a folder Shikhar1998/Basic-Facebook-Notifications-Reminder in your Local Drive.
 
Now installing all the packages required for this project :

`""cd/Basic-Facebook-Notifications-Reminder `

`pip install -r requirements.txt""`
 
This will install the packages from the internet otherwise show ""Requirment already satisfied""

####2. Linking Facebook and Python  :
1. Login to your Facebook Account.

2. Create a New Facebook App : https://developers.facebook.com/docs/graph-api
 
3. Now open the link : https://developers.facebook.com/tools/explorer

4. In the application bar select your app and then click "Get User Access Token" from the "Get Token" option.
 
5. Copy the access token and open the file in python - main.py in the folder  "Basic-Facebook-Notifications-Reminder" and in line 9 enter the App Token.
 
 
####3. Connect the Arduino and the LCD Screen 
1 . Solder the pin headers to the LCD Display.
 
2 . Make the following connection to the arduino and the LCD Screen.
 


####3. Features :

1. Highly automated and requires only one time configuration.
2. Easily can be implemented to notify you for posts from a particular group or page.
3. Will automatically display any new posts after every 10 minutes and also display the most recent message along with the sender's name.
 
 
####4. Issues :
Any improvements or issues : https://github.com/Shikhar1998/Basic-Facebook-Notifications-Reminder
Please report or open a new issue.


####5. Future Upgrades Possible : 
1. Linking Gmail and Twitter similarly with Arduino using Gmail API v1
For Gmail (https://developers.google.com/gmail/api/v1)  
For Twitter (https://dev.twitter.com/rest/public)

Thank You

Any Improvements :Feel free to ping!!
     

