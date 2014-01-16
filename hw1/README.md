Homework 1
=====

Use mongorestore to restore the dump into your running mongod. Do this by opening a terminal window (mac) or cmd window (windows) and navigating to the directory so that the dump directory is directly beneath you. Now type
```
mongorestore dump
```

Now, using the Mongo shell, perform a findone on the collection called hw1 in the database m101. That will return one document. Please provide the value corresponding to the "answer" key from the document returned.
```
> use m101 
> var j = db.hw1.findOne() 
> j["answer"]
```


