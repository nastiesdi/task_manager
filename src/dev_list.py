class DevList:
    def __init__(self):
        self.devs = dict()

    def __str__(self):
        return str([{dev.email for dev in self.devs.values()}, {dev.uid for dev in self.devs.values()}])

    def add_dev(self, dev):
        if isinstance(dev, list):
            for item in dev:
                self.devs[item.uid] = item
        else:
            self.devs[dev.uid] = dev

    def get_all_email(self):
        print([dev.email for dev in self.devs.values()])
