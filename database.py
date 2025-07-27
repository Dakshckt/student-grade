import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["studentGradeSystem"]
mycol = mydb["students"]

print("Connected")