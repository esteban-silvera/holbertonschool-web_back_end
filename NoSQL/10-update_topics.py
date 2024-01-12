#!/usr/bin/env python3
"""comentarius"""


def update_topics(mongo_collection, name, topics):
    """Function that update a document."""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})