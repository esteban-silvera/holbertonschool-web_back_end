#!/usr/bin/env python3
"""comentarius"""


def list_all(mongo_collection):
    """comentondo"""
    documents = mongo_collection.find()
    if not documents:
        return []
    return documents
