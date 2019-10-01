import time
from abc import ABC


class MainClass(ABC):
    def __init__(self):
        self.created_at = time.strftime('%X, %x', time.localtime())
        self.updated_at = 'Not changed'

    def update_time(self):
        self.updated_at = time.strftime('%X, %x', time.localtime())

    def get_time(self):
        return self.created_at, self.updated_at