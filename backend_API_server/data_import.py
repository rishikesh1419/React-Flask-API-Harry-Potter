import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["potterdb"]
files = ["characters", "houses", "spells"]

for f in files:
    coll = mydb[f]
    with open(f"HP_Data/{f}.json") as file:
        file_data = json.load(file)
    if isinstance(file_data, list):
        coll.insert_many(file_data)
    else:
        coll.insert_one(file_data)
