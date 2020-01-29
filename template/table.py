from template.page import *
from time import time

INDIRECTION_COLUMN = 0
RID_COLUMN = 1
TIMESTAMP_COLUMN = 2
SCHEMA_ENCODING_COLUMN = 3


class Record:

    def __init__(self, rid, key, columns, se):
        self.rid = rid
        self.key = key
        self.columns = columns
        self.indirection = 0
        self.schema_encoding = se
        self.timestamp = time()


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
        pass

    def create_page(self):
        Page()

    def __merge(self):
        pass
 
