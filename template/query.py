from template.table import Table, Record
from template.index import Index
from template.config import *

PAGE_RANGE_AMT = 0  # Current # of page ranges
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

        # Create new base record
        b_record = Record(BASE_RID, self.table.key, columns)
        BASE_RID += 1  # update RID value for next insert
        b_pages = self.table.base_pages

        # If base pages full, add new ones
        if not b_pages[len(b_pages) - len(columns) - 4].has_capacity():
            for col in range(0, self.table.num_columns + 4):
                self.table.base_pages.append(self.table.create_page())

        # Get indices of base pages
        in_col = len(b_pages) - len(columns) - 4
        rid_col = len(b_pages) - len(columns) - 3
        time_col = len(b_pages) - len(columns) - 2
        se_col = len(b_pages) - len(columns) - 1

        # Write to base pages at appropriate offset
        b_pages[in_col].write(b_record.indirection)
        b_pages[rid_col].write(b_record.rid)
        b_pages[time_col].write(int(b_record.time_stamp))
        b_pages[se_col].write(int(schema_encoding))

        for col_index in range(0, len(columns)):
            b_pages[len(b_pages) - len(columns) + col_index].write(columns[col_index])

        # Insert RID - 1st page location into the page directory
        self.table.index_map.update({columns[self.table.key]: b_record.rid})

        # Gives starting bit of record entry in 1st column
        offset = (b_pages[in_col].records() - 1) * 8
        self.table.page_directory.update({b_record.rid: (in_col, offset)})

        # Check if page range exceeded
        global PAGE_RANGE_AMT
        if b_record.rid % PAGE_RANGE_SIZE == 1:
            PAGE_RANGE_AMT += 1
            self.table.page_range.update({b_record.rid % PAGE_RANGE_SIZE + PAGE_RANGE_AMT - 2: (
            PAGE_RANGE_AMT, -1)})  # Tuple is pg range # and loc in tailpgs

    """
    # Read a record with specified key
    """

    def select(self, key, query_columns):
        pass

    """
    # Update a record with specified key and columns
    """

    def update(self, key, *columns):  # Non-cumulative updates
        global TAIL_RID

        # Get location of base record via index map
        base_rid = self.table.index_map.get(key)

        # Get starting column location in b_pages and offset of base record
        tup = self.table.page_directory.get(base_rid)

        # Create new tail record
        tail_record = Record(TAIL_RID, self.table.key, columns)
        TAIL_RID += 1

        # Retrieve tail pages or create new ones
        page_rg = int(base_rid / PAGE_RANGE_SIZE)
        tail_page = self.table.page_range.get(page_rg)

        # If no tail pages for current page range, create more
        if tail_page[1] == -1:
            for col in range(0, self.table.num_columns + 4):
                self.table.tail_pages.append(self.table.create_page())

        # Change indirection and SE in base record
        se = ''
        for i in range(0, self.table.num_columns):
            if columns[i]:
                se += '1'
            else:
                se += '0'

        # If tail pages at capacity, create more

        # Write to tail pages

        # New RID to give to tail record
        tail_rid = TAIL_RID

        pass

    """
    :param start_range: int         # Start of the key range to aggregate 
    :param end_range: int           # End of the key range to aggregate 
    :param aggregate_columns: int  # Index of desired column to aggregate
    """

    def sum(self, start_range, end_range, aggregate_column_index):
        pass