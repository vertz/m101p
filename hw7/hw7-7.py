import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the photosharing database
db=connection.photosharing
albums = db.albums
images = db.images

# remove every image from the images collection that appears in no album. 
def find():

    query = {}
    selector = { '_id': 1 }

    try:
        cursor = images.find(query, selector)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    for doc in cursor:
        
        try:
            image_id = doc['_id']
            n_albums = albums.find({'images': image_id}).count()
            
            if n_albums < 1:
                images.remove({"_id": image_id}) 

        except:
            print "Unexpected error:", sys.exc_info()[0]   


find()
