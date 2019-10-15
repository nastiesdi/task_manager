
def create_list_vision(smth):
    return smth.replace("'", "").replace("),", "\n").replace("(", "").replace(",", ":").replace("[", " ").replace(")", " ").strip("[]")


def try_it(field):
    return str(list(enumerate(field, start=1))).replace("'", "").replace("),", "\n").replace("(", "").replace(",", ":").replace("[", " ").replace(")", " ").strip("[]")
