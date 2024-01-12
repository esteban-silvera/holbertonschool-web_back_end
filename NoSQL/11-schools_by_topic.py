#!/usr/bin/env python3
"""comentarius"""


def schools_by_topic(mongo_collection, topic):
    """comentondo"""
    return mongo_collection.find({"topics": topic})
