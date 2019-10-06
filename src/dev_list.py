class DevList:
    def __init__(self):
        self.devs = dict()

    def __str__(self):
        return print({dev.email for dev in self.devs.values()}, {dev.uid for dev in self.devs.values()})

    def add_dev(self, dev):
        # if isinstance(dev, list):
        #     for item in dev:
        #         self.devs[item.uid] = item почему не могу так сделать
        self.devs[dev.uid] = dev

    def get_all_email(self):
        return print({dev.email for dev in self.devs.values()}) # каk он понимает что есть майл у дева если нет импорта
