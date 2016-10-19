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
###<ul><li>
<b>1.Register new user:</b>
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
</li>


###<li><b>2.Login registered user:</b>
<li> URL: http://awasthikamal97.pythonanywhere.com/location/login</li>
<li>Fields names and values:
<ol>
<li>'username' : "example_username"</li>
<li>'password' : "example_password"</li>
</ol></li>
<li> username and password will be authenticated and response will be returned</li>
<li> Response: 
<ol>if credentials are valid: "login successful"</ol>
<ol>If credentials are invalid: "invalid credentials"</ol>
</li>
<li> POST request values are to be sent in test form(not JSON)</li>
<li>
</ul>



