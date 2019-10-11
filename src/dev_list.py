class DevList:
    def __init__(self):
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
        return 'Our developer: \n' + str(list(zip(range(1, len(self.devs)+1), a))).replace("'", "").replace("),", "\n").replace("(", "").replace(",",":").replace("[", " ").replace(")]", " ")

    def get_all_email(self):
        print([dev.email for dev in self.devs.values()])
