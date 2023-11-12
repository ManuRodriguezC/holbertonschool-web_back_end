#!/usr/bin/env python3
"""This module call elements of db an collection"""
from pymongo import MongoClient


methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
client = MongoClient('mongodb://127.0.0.1:27017')
db = client.logs
if "nginx" in db.list_collection_names():  
    collection = db.nginx

    count = collection.count_documents({})

    print(f"{count} logs")

    print("Methods:")

    for method in methods:
        met = collection.count_documents({"method": method})
        print(f"    method {method}: {met}")   
