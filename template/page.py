from template.config import *

class Page:

    def __init__(self):
        self.num_records = 0
        self.data = bytearray(4096)

    def has_capacity(self):
        return self.num_records <= MAX_RECORDS

    """
    Since each column will be at max a 64 bit integer, we can index the bytearray
    from page by a slice of 8 bytes and add values to those specific slices.

    NOTE: let a be an integer,
        (a).to_bytes(length=8,byteorder='big') turns an integer into its 8 byte representation
    """

    def write(self, value):
        self.data[(self.num_records * 8):(self.num_records * 8) + 8] = value.to_bytes(length=8, byteorder='big')
        self.num_records += 1
        pass
