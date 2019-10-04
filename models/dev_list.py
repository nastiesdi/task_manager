class DevList:
    def __init__(self, dev):
        self.devs = dict()
        self.devs[dev.uid] = dev

    def add_dev(self, dev):
        self.devs[dev.uid] = dev

    def get_all_email(self):
        return {dev.email for dev in self.devs.values()}


devlist = DevList
