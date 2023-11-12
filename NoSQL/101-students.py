#!/usr/bin/env python3
""" This module sorh an return documents """
from pymongo import DESCENDING


def top_students(mongo_collection):
    """
    Retrieves all students sorted by their average scores.
    --------
    Args:
        mongo_collection: The MongoDB collection object containing the student documents.
        
    Returns:
        list: A list of student documents, sorted by the average of their scores in descending order.
        Each document includes an additional field 'averageScore' representing the average score of the student.
    """
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "topics": {"$push": "$topics"},
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": DESCENDING}}
    ]

    result = list(mongo_collection.aggregate(pipeline))

    for doc in result:
        doc['averageScore'] = doc['averageScore']

    return result
