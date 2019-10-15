import re

from src.main_class import MainClass


class DevList(MainClass):
    def __init__(self):
        super().__init__()
        self.devs = dict()

    def add_dev(self, dev):
        if isinstance(dev, list):
            for item in dev:
                self.devs[item.uid] = item
        else:
            self.devs[dev.uid] = dev

    def __str__(self):
        display = 'All dev:\n'
        for i, j in enumerate([dev.email for dev in self.devs.values()], start=1):
            display += str(i) + ': ' + str(j) + '\n'
        return display




