#!/usr/bin/env python3
"""This module call elements of db an collection"""
from pymongo import MongoClient


methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
client = MongoClient('mongodb://127.0.0.1:27017')
db = client.logs
if "nginx" in db.list_collection_names(): 
    collection = db.nginx

    count = collection.count_documents({}) if collection.count_documents({}) != 0 else 0

    print(f"{count} logs")

    print("Methods:")

    for method in methods:
        met = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {met}")
    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")
