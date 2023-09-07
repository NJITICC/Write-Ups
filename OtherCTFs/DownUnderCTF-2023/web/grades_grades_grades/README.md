# DUCTF 2023 - grades_grades_grades

## TL;DR

Sign up and see those grades :D! How well did you do this year's subject? 
Author: donfran

## Approach

In this challenge, you are given access to a website. The website seems to only have a signup option at first glance. 
Initially, it is good to go through the motions as an average user would to see what is available to us. The register page may be susceptible to either SQL or NoSQL however, looking at the provided source code, the auth.py file stood out the most.

This file was the handler for sessions using JWT (JSON Web Tokens). There are a collection of vulnerabilities for JWT. The other important step I noticed was in routes.py; the flag was present under /grades_flag. 

```
@api.route('/grades_flag', methods=('GET',))
@requires_teacher
def flag():
    return render_template('flag.html', flag="FAKE{real_flag_is_on_the_server}", is_auth=True, is_teacher_role=True)
```

when registering, our session was assigned a user access level to studnet (in this, is_teacher_role=False) but we cannot access the flag as a student. 

```
is_teacher_role=True
```
This being my first time working with JWT, it was a great introduction to it. 

1. The key was randomly generated, I would not imagine we were expected to brute force the key, this would be impossibly time consuming and resource intensive. 
```
SECRET_KEY = secrets.token_hex(32)
```
2. The token creation did not have any validation on the data coming from the request. This was the vulnerability.

The POST request for registration was passing these variables to the application. 
```
stu_num=testing&stu_email=testing%40te&password=testing
```
Knowing this and that the data from the request was not being sanatized.
```
def create_token(data):
    token = jwt.encode(data, SECRET_KEY, algorithm='HS256')
    return token
``` 
In combination with this website tool, https://jwt.io/, you are able to see what data the token stored. They were identical to the variables in the POST request. 
Since the variables were identical and they were being passed along in data with any sanatization, you were able to specify the is_teacher variable in the request and set it as true.

## Solution

Add the "is_teacher=True" to the variables in the POST request. 
```
stu_num=testing&stu_email=testing%40te&password=testing&is_teacher=True
```
## Flag

FLAG: DUCTF{Y0u_Kn0W_M4Ss_A5s1GnM3Nt_c890ne89c3}

## Acknowledgments

Tom B & Alfred S 

---


