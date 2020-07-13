"""
Connect to the MongoDB database potterdb
"""

from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/")

mydb = myclient["potterdb"]