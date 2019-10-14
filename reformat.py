class str_(str):
    def create_list_vision(self):
        return str(self).replace("'", "").replace("),", "\n").replace("(", "").replace(",", ":").replace("[", " ").replace(")", " ").strip("[]")


