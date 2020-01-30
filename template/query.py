from template.table import Table, Record
from template.index import Index
from template.config import *

BASE_RID = 1
TAIL_RID = 2 ** 64 - 1


class Query:
    """
    # Creates a Query object that can perform different queries on the specified table
    """

    def __init__(self, table):
        self.table = table
        pass

    """
    # internal Method
    # Read a record with specified RID
    """

    def delete(self, key):
        pass

    """
    # Insert a record with specified columns
    """

    def insert(self, *columns):

        schema_encoding = '0' * self.table.num_columns

        global BASE_RID
        record = Record(BASE_RID, self.table.key, columns)
        BASE_RID += 1  # update RID value for next insert
        pages = self.table.base_pages

        in_col = len(pages) - len(columns) - 4
        rid_col = len(pages) - len(columns) - 3
        time_col = len(pages) - len(columns) - 2
        se_col = len(pages) - len(columns) - 1

        if pages[in_col].has_capacity():
            pages[in_col].write(record.rid)
            pages[rid_col].write(record.indirection)
            pages[time_col].write(int(schema_encoding))
            pages[se_col].write(int(record.time_stamp))
            for col_index in range(0, len(columns)):
                pages[len(pages) - len(columns) + col_index].write(columns[col_index])

    """
    # Read a record with specified key
    """

    def select(self, key, query_columns):
        pass

    """
    # Update a record with specified key and columns
    """

    def update(self, key, *columns):
        global TAIL_RID
        # Insert into tail page here
        TAIL_RID += 1
        pass

    """
    :param start_range: int         # Start of the key range to aggregate 
    :param end_range: int           # End of the key range to aggregate 
    :param aggregate_columns: int  # Index of desired column to aggregate
    """

    def sum(self, start_range, end_range, aggregate_column_index):
        pass