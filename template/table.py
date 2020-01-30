from template.page import *
from time import time
from template.config import *

class Record:

    def __init__(self, rid, key, columns):
        self.rid = rid
        self.key = key
        self.columns = columns
        self.indirection = 0
        self.time_stamp = time()

class Table:

    """
    :param name: string         #Table name
    :param num_columns: int     #Number of Columns: all columns are integer
    :param key: int             #Index of table key in columns
    """
    def __init__(self, name, key, num_columns):
        self.name = name
        self.key = key
        self.num_columns = num_columns
        self.page_directory = {}
        self.base_pages = []
        self.tail_pages = []
        pass

    def create_page(self):
        return Page()

    def __merge(self):
        pass