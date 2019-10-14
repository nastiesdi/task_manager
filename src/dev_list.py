from src.main_class import MainClass
from helpers.reformat import create_list_vision


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
        a = []
        for dev in self.devs.values():
            a.append(str(dev.email).strip("\'"))
        return 'Our developer: \n' + create_list_vision(str(list(zip(self.get_len_str(self.devs), a))))

    def get_all_email(self):
        a = [dev.email for dev in self.devs.values()]
        return 'Our developer: \n' + create_list_vision(str(list(zip(self.get_len_str(self.devs), a))))
