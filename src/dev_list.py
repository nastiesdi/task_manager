import re

from src.main_class import MainClass


class DevList(MainClass):
    def __init__(self):
        super().__init__()
        self.devs = dict()

    def __str__(self):
        display = 'All dev:\n'
        for num, email in enumerate([dev.email for dev in self.devs.values()], start=1):
            display += str(num) + ': ' + str(email) + '\n'
        return display

    def add_dev(self, dev):
        if isinstance(dev, list):
            for item in dev:
                self.devs[item.uid] = item
        else:
            self.devs[dev.uid] = dev
