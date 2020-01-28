from template.table import Table, Record
from template.index import Index

class Query:
    """
    # Creates a Query object that can perform different queries on the specified table 
    """

    def __init__(self, table):
        self.table = table
        self.RID = 1
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

        record = Record(self.RID, self.table.key, columns)
        self.RID += 1   # update RID value for next insert
        pages = self.table.base_pages
        """
        Since each column will be at max a 64 bit integer, we can index the bytearray
        from page by a slice of 8 bytes and add values to those specific slices.
            
        NOTE: let a be an integer,
            (a).to_bytes(length=8,byteorder='big') turns an integer into its 8 byte representation
        """
        for index in range(0,4096,8):
            bvalue = pages['RID'].data[index:index+8]
            if int.from_bytes(bvalue, byteorder='big') == 0:
                pages['RID'].data[index:index + 8] = (record.rid).to_bytes(length=8,byteorder='big')
                pages['Indirection'].data[index:index + 8] = (record.indirection).to_bytes(length=8,byteorder='big')
                pages['Schema Encoding'].data[index:index + 8] = int(schema_encoding).to_bytes(length=8,byteorder='big')
                pages['Start Time'].data[index:index + 8] = int(record.time_stamp).to_bytes(length=8,byteorder='big')
                """
                This for loop goes through the actual data and adds them to there respective base pages
                """
                for col in range(0, len(columns)):
                    pages[str(col)].data[index:index + 8] = (columns[col]).to_bytes(length=8,byteorder='big')
                break

    """
    # Read a record with specified key
    """

    def select(self, key, query_columns):
        pass

    """
    # Update a record with specified key and columns
    """

    def update(self, key, *columns):
        pass

    """
    :param start_range: int         # Start of the key range to aggregate 
    :param end_range: int           # End of the key range to aggregate 
    :param aggregate_columns: int  # Index of desired column to aggregate
    """

    def sum(self, start_range, end_range, aggregate_column_index):
        pass
