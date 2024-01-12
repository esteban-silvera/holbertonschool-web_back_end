#!/usr/bin/env python3
"""comentarius"""


def insert_school(mongo_collection, **kwargs):
    """comentondo"""
    object_inserted = mongo_collection.insert_one(kwargs)
    return object_inserted.inserted_id