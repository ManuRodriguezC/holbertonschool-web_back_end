#!/usr/bin/env python3
"""This module update elemets in one collection"""


def update_topics(mongo_collection, name, topics):
    """
    This function update one element in any collection.
    ----------------
    Parameters:
        mongo_collection: The name of the collection in database.
        name: The name of the attribute in collection.
        topics: The value of the new attribute.
    Return:
        None
    """
    mongo_collection.update_one({"name": name}, { "$set": { "topics": topics}})
