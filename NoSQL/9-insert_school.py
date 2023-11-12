#!/usr/bin/env python3
"""Module insert elements in collection"""


def insert_school(mongo_collection, **kwargs):
    """
    This function insert one element in any collection
    ----------
    Parameters:
        mongo_collection: Name of the collection
        into wich the element is inserted.
        kwarg: Dates that inserted into collection.
    Return:
        The id of the new element.
    """
    new_date = mongo_collection.insert_one(kwargs)
    return new_date.inserted_id
