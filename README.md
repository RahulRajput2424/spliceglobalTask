# SpliceglobalTask

Step 1. Make a directory spliceGlobalTask <br />
Step 2. create a virtual env using below command inside spliceGlobalTask folder <br />
**python3 -m venv splicenv<br />**
Step 4. Now clone the project using git clone <br />
Step 5. Install all the dependency using pip3 install requirements.txt<br />
Step 6. Run server using python3 manage.py runserver

For the registration, **user_type value 1**  is used for vendor and **user_type value 2** is used for Bidder.



1- SignUp: URL: http://127.0.0.1:8000/spiceApp/user_signup_view/ Method - Post Param = { "user_type":1, "email":"user@gmail.com", "mobileNumber":7858588481, "username":"user1", "password":"user" }

2- Login: URL: http://127.0.0.1:8000/spiceApp/user_login_view/ Method: POST Body Param: { "email":"user@gmail.com", "password":"user" }

