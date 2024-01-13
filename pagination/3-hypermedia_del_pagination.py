#!/usr/bin/env python3
"""coments"""
import csv
import math
from typing import List, Dict, Any


def index_range(page, page_size):
    """comentariu"""
    if page and page_size:
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index


class Server:
    """coment class"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """function coment"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """coments"""
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        start, end = index_range(page, page_size)
        pages = []
        if start >= len(self.dataset()):
            return pages
        pages = self.dataset()
        return pages[start:end]

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ coments"""
        assert type(index) == int and type(page_size) == int
        assert 0 <= index < len(self.indexed_dataset())
        pages = []
        next_index = index + page_size
        for i in range(index, index + page_size):
            if not self.indexed_dataset().get(i):
                i += 1
                next_index += 1
            pages.append(self.indexed_dataset()[i])
        return {'index': index,
                'next_index': next_index,
                'page_size': page_size,
                'data': pages
                }
