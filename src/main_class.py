import datetime
from abc import ABC


class MainClass(ABC):
    def __init__(self):
        self.created_at = datetime.datetime.now()
        self.updated_at = 'Not changed'

    def update_time(self):
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return f'{self.created_at}, {self.updated_at}'

    def get_time(self):
        print(f'created at: {self.created_at}, updated_at: {self.updated_at}')
