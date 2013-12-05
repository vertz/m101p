import pymongo
import sys

# establish a connection to the database
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the students database
db=connection.students
grades = db.grades

def remove(_id):

    query = {'_id' : _id}
    
    try:
        grades.remove(query)

    except:
        print "Unexpected error:", sys.exc_info()[0]

# remove the grade of type "homework" with the lowest score for each student 
# from the dataset that you imported in HW 2.1
def find():

    query = {"type" : "homework"}

    try:
        cursor = grades.find(query)
        cursor = cursor.sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])

    except:
        print "Unexpected error:", sys.exc_info()[0]

    student_id = None

    for doc in cursor:
        
        if student_id != doc['student_id']:
            remove(doc['_id']) 
            student_id = doc['student_id']   


find()
