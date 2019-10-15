from src.main_class import MainClass
from helpers.reformat import create_list_vision
from helpers.reformat import  try_it


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
        a = [dev.email for dev in self.devs.values()]
        return 'Our developer: \n' + try_it(a)

    def get_all_email(self):
        a = [dev.email for dev in self.devs.values()]
        return 'Our developer: \n' + try_it(a)
