import pymongo
import os


import certifi
ca = certifi.where()

class MongodbOperation:

    def __init__(self) -> None:

        self.client = pymongo.MongoClient('mongodb+srv://rajan98:rajan98@cluster0.rw7fcy2.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
        self.db_name="ineuron"

    def insert_many(self,collection_name,records:list):
        self.client[self.db_name][collection_name].insert_many(records)

    def insert(self,collection_name,record):
        self.client[self.db_name][collection_name].insert_one(record)
        
