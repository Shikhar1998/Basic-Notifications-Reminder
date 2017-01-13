#Facebook-Feed-Notification-Display

**About The Project**: 

This application is used to display the recent notifications(on feed) of Facebook on a LCD Display.

**Contents**:

1. [Requirements](#requirements)

2. [Installation](#installation)

3. [Working](#working)

#### Requirements:

1 . Facebook ID 

2 . Allowing access to Graph API.

3 . Arduino UNO

4 . LCD Display

#### Installation :

1. Installing the Package :

     git clone https://github.com/Shikhar1998/Basic-Facebook-Notifications-Reminder.git && cd fb/
     pip install -r requirements.txt
     
2. Getting Facebook Access Token :

     1 . Open https://developers.facebook.com/apps/ and Create an App
     
     2 . Follow steps below 
     
     ![](screen.gif?raw=true)
  
3. Connect the LCD screen to Arduino

4.   python scheduer.py
          
### Working :

1. Extracts data from fb using Facebook Graph API

2. Check from log when last data was collected and the time seperation from most recent feed post and the log data file.

3. Fetch the number of new posts and the most recent post.

4. Send the data to Arduino connected to LCD Screen which displays it.


Thank You

Any Improvements :Feel free to ping!!
     

