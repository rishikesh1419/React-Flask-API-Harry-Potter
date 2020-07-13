import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["potterdb"]

# coll = mydb["characters"]
# coll = mydb["houses"]
coll = mydb["spells"]

# with open("HP_Data/characters.json") as file:
# with open("HP_Data/houses.json") as file:
with open("HP_Data/spells.json") as file:
    file_data = json.load(file) 
 
if isinstance(file_data, list): 
    coll.insert_many(file_data)   
else: 
    coll.insert_one(file_data) 