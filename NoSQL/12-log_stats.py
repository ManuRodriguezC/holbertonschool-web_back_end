#!/usr/bin/env python3
"""This module call elements of db an collection"""
from pymongo import MongoClient


methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
client = MongoClient('mongodb://127.0.0.1:27017')
db = client.logs.nginx

count = db.count_documents({})

if count >= 0:
    print(f"{count} logs")

    print("Methods:")

    for method in methods:
        met = db.count_documents({"method": method})
        print(f"    method {method}: {met}")   
