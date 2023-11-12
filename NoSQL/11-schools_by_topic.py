#!/usr/bin/env python3
"""This module call the dates with specific values"""


def schools_by_topic(mongo_collection, topic):
    """
    This funcion return list of elemets that contein one date.
    ------------
    Parameters:
        mongo_collection: The name of teh collection in db.
        topic: The date with find in collection.
    Return:
        List of elements with topic value.
    """
    dates = mongo_collection.find({ "topics": {"$in": [topic]}})
    return dates
