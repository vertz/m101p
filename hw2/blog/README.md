Homework 2.3
=====

The project roughly follows the model/view/controller paradigm. userDAO and sessionDAO.py comprise the model. blog.py is the controller. The templates comprise the view.

If everything is working properly, you should be able to start the blog by typing:
```
python blog.py
```

Note that this project requires the following python modules be installed on your computer: cgi, hmac, re, datetime, random, json, sys, string, hashlib, bson, urllib, urllib2, random, re, pymongo, and bottle. A typical Python installation will already have most of these installed except pymongo and bottle.

If you goto http://localhost:8082 you should see a message “this is a placeholder for the blog”

Here are some URLs that must work when you are done.
```
http://localhost:8082/signup
http://localhost:8082/login
http://localhost:8082/logout
```

When you login or sign-up, the blog will redirect to http://localhost:8082/welcome and that must work properly, welcoming the user by username

We have removed two pymongo statements from userDAO.py and marked the area where you need to work with XXX. You should not need to touch any other code. The pymongo statements that you are going to add will add a new user upon sign-up and validate a login by retrieving the right user document.

The blog stores its data in the blog database in two collections, users and sessions. Here are two example docs for a username ‘erlichson’ with password ‘fubar’. You can insert these if you like, but you don’t need to.
```
> db.users.find()
{ "_id" : "erlichson", "password" : "d3caddd3699ef6f990d4d53337ed645a3804fac56207d1b0fa44544db1d6c5de,YCRvW" }
> 
> db.sessions.find()
{ "_id" : "wwBfyRDgywSqeFKeQMPqVHPizaWqdlQJ", "username" : "erlichson" }> 
```
