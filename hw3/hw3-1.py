import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the students database
db=connection.school
students = db.students

# remove the lowest homework score for each student. 
def find():

    query = {}

    try:
        cursor = students.find(query)

    except:
        print "Unexpected error:", sys.exc_info()[0]

    for doc in cursor:
        
        try:
            scores = doc['scores']
            
            to_remove = None
            min_score = float("infinity")
            
            for dic in scores:
                if dic['type'] == "homework":
                    score = float(dic['score'])
                    
                    if min_score > score:
                        to_remove = dic
                        min_score = score   
            
            if to_remove:
                scores.remove(to_remove) 
                students.update({'_id':doc['_id']}, {'$set':{'scores':scores}}) 

        except:
            print "Unexpected error:", sys.exc_info()[0]   


find()
