import time
from abc import ABC


class MainClass(ABC):
    def __init__(self):
        self.created_at = time.strftime('%X, %x', time.localtime())
        self.updated_at = None
        super().__init__()
