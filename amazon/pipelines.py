# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

# Mongo DB :)

class AmazonPipeline:
    def __init__(self):
        self.conn = pymongo.MongoClient("mongodb+srv://root:<password>@amazonproduct.h0t1opc.mongodb.net/?retryWrites=true&w=majority") # mongo db connection

        db = self.conn["AmazonProduct"] # mongo db database
        db.drop_collection("product_tb") # mongo db collection(table) remove

        self.collection = db["product_tb"] # mongo db collection(table) create
    def process_item(self, item, spider):
        self.collection.insert_one(dict(item)) # mongo db data save
        return item
