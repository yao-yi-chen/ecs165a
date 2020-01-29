from template.table import Table

class Database():

    def __init__(self):
        self.tables = []
        pass

    def open(self):
        pass

    def close(self):
        pass

    """
    # Creates a new table
    :param name: string         #Table name
    :param num_columns: int     #Number of Columns: all columns are integer
    :param key: int             #Index of table key in columns
    """
    def create_table(self, name, key, num_columns):
        table = Table(name, key, num_columns)
        """
        update the base_pages field that was added in the table.py file
        """
        table.base_pages.update({'RID': table.create_page(), 'Indirection': table.create_page(),
                                 'Schema Encoding': table.create_page(), 'Start Time': table.create_page(),
                                 'key': table.create_page()})
        for col in range(0, num_columns):
            table.base_pages.update({str(col): table.create_page()})
        return table

    """
    # Deletes the specified table
    """
    def drop_table(self, name):
        pass

#        self.rid = rid
#        self.key = key
#        self.columns = columns
#        self.indirection = 0
#        self.schema_encoding = schema_encoding
#        self.time_stamp = time()