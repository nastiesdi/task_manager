import datetime
from abc import ABC


class MainClass(ABC):
    def __init__(self):
        self.created_at = datetime.datetime.now()
        self.updated_at = 'Not changed'
        self.m = int

    def update_time(self):
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f'{self.created_at}, {self.updated_at}'

    def get_time(self):
        return f'created at: {self.created_at}, updated_at: {self.updated_at}'

    def get_len_str(self, field):
        self.m = list(range(1, len(field) + 1))
        return self.m

