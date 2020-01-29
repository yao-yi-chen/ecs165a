from template.config import *

MAX_RECORDS = 512

class Page:

    def __init__(self):
        self.num_records = 0
        self.data = bytearray(4096)

    def has_capacity(self):
        return self.num_records <= MAX_RECORDS

    def write(self, value):
        self.data[(self.num_records * 8):(self.num_records * 8) + 8] = value.to_bytes(length=8, byteorder='big')
        self.num_records += 1
        pass

