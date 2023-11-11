#!/usr/bin/env python3
""" This module return list of elements in collection"""


def list_all(mongo_collection):
    """
    This function return all elements in specific collection
    --------------
    params:
        mongo_collection: Name of the collection in mongodb.
    return:
        List of elements if exist or empty list.
    """
    elements = list(mongo_collection.find())
    if not elements:
        return []
    return elements
