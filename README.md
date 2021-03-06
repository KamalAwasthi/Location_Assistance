# Location_Assistance

Location Assistance is location based service with features like:

1. One to one location sharing
2. Location + Activity sharing with friends.
3. Location based reminders.
4. Location based automatic mobile settings.

<hr>
The project is in its intial development phase, product will be ready soon :+1: :smile:

#API Guidelines:

##Register Table
###<b>1.New user registration:</b>
<ul>
    <li> URL: http://awasthikamal97.pythonanywhere.com/location/registration </li>
    <li>Fields names and values:
        <ol>
            <li>'username' : "example_username"</li>
            <li>'password' : "example_password"</li>
            <li>'first_name' : "example_name"</li>
            <li>'last_name' : "example_name"</li>
        </ol>
    </li>
    <li> password will be saved a hash</li>
    <li> Response: 
    <ol>if username is already registered: "username already taken"</ol>
    <ol>Sucessful Registration: "registration successful"</ol>
    </li>
    <li> POST request values are to be sent in test form(not JSON)</li>
</ul>


###<b>2.Login registered user:</b>
<ul>
    <li> URL: http://awasthikamal97.pythonanywhere.com/location/login</li>
    <li>Fields names and values:
        <ol>
            <li>'username' : "example_username"</li>
            <li>'password' : "example_password"</li>
         </ol>
     </li>
    <li> username and password will be authenticated and response will be returned</li>
    <li> Response: 
        <ol>if credentials are valid: "login successful"</ol>
        <ol>If credentials are invalid: "invalid credentials"</ol>
    </li>
    <li> POST request values are to be sent in test form(not JSON)</li>
</ul>


##SaveSettings Table
###<b>1.Set New Settings</b>
<ul>
    <li>URL: http://awasthikamal97.pythonanywhere.com/location/set_settings</li>
    <li>Field names and values:
        <ol>
            <li>'longitude' : '23.76986543' - (decimal value, 8 digits after decimal and 2 digits before decimal)</li>
            <li> 'latitude' : '34.78905634' - (decimal value, 8 digits after decimal and 2 digits before decimal) </li>
            <li> 'volumeLevel' : '4.5' - (decimal value) </li>
            <li> 'vibrationMode' : 'True' - (Boolean Value) </li>
            <li> 'brightness' : '6.7' - (decimal value) </li>
            <li> 'mobileData' : 'True' - (Boolean Value)</li>
            <li> 'wifi' : 'True' - (Boolean Value)</li>
            <li> 'bluetooth' : 'True' - (Boolean Value)</li>
            <li>'username' : "kamal' - (Character Field)</li>
            <li> 'activity' : "going for shopping" - (Text Value)</li>
        </ol>
    </li>
    <li> after the user authenctication, settings will be saved</li>
    <li> Response: 
        <ol>sucessful save: "settings saved"</ol>
        <ol>error in input: "error in user input"</ol>
        <ol>If username is does not found in database: "username not registered"</ol>
    </li>
</ul>  

###<b>2.SyncSettings</b>
<ul>
    <li>URL: http://awasthikamal97.pythonanywhere.com/location/sync_settings</li>
    <li>Field names and values:
        <ol>
            <li>'username' : "kamal' - (Character Field)</li>
        </ol>
    </li>
    <li> after the user authenctication, settings will be filtered on the basis of username</li>
    <li> Response: 
        <ol>response: setiings list in JSON form</ol>
        <ol>If username is does not found in database: "username not registered"</ol>
    </li>
</ul> 


##Live Table
###<b>1.Record Live Status</b>
<ul>
    <li>URL: http://awasthikamal97.pythonanywhere.com/location/set_status</li>
    <li>Field names and values:
        <ol>
            <li>'longitude' : '23.76986543' - (decimal value, 8 digits after decimal and 2 digits before decimal)</li>
            <li> 'latitude' : '34.78905634' - (decimal value, 8 digits after decimal and 2 digits before decimal) </li>
            <li>'username' : "kamal' - (Character Field)</li>
            <li> 'time' : "2016-10-19 12:34:12" - (DateTime Field)</li>
        </ol>
    </li>
    <li> after verifying the username, live status would be recorded</li>
    <li> Response: 
        <ol>sucessful save: "live status recorded"</ol>
        <ol>If username is does not found in database: "username not registered"</ol>
    </li>
</ul> 



##Reminder Table
###<b>1.Set Reminder</b>
<ul>
    <li>URL: http://awasthikamal97.pythonanywhere.com/location/set_reminder</li>
    <li>Field names and values:
        <ol>
            <li>'longitude' : '23.76986543' - (decimal value, 8 digits after decimal and 2 digits before decimal)</li>
            <li> 'latitude' : '34.78905634' - (decimal value, 8 digits after decimal and 2 digits before decimal) </li>
            <li>'username' : "kamal' - (Character Field)</li>
            <li> 'reminder_title' : "Buy Milk" - (Character Field)</li>
            <li> 'reminder_text' : "Buy milk from here, this place is really good" - (Text Field)</li>
        </ol>
    </li>
    <li> after verifying the username, reminder  would be recorded</li>
    <li> Response: 
        <ol>sucessful save: "reminder has been set"</ol>
        <ol>If username is does not found in database: "username not registered"</ol>
    </li>
</ul> 

###<b>2.Sync Reminders</b>
<ul>
    <li>URL: http://awasthikamal97.pythonanywhere.com/location/sync_reminders</li>
    <li>Field names and values:
        <ol>
            <li>'username' : "kamal' - (Character Field)</li>
        </ol>
    </li>
    <li> after the user authenctication, settings will be filtered on the basis of username</li>
    <li> Response: 
        <ol>Response: User's reminders in JSON form </ol>
        <ol>If username is does not found in database: "username not registered"</ol>
    </li>
</ul> 


###<b>2.Delete Reminder</b>
<ul>
    <li>URL: http://awasthikamal97.pythonanywhere.com/location/elete_reminder</li>
    <li>Field names and values:
        <ol>
            <li>'username' : "kamal' - (Character Field)</li>
            <li> 'id' : "12" - (Integer Field)</li>
        </ol>
    </li>
    <li> after verifying the username, reminder  would be deleted</li>
    <li> Response: 
        <ol>sucessful save: "reminder deleted sucessfull"</ol>
        <ol>If username is does not found in database: "username not registered"</ol>
    </li>
</ul> 

