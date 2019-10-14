
def create_list_vision(smth):
    return smth.replace("'", "").replace("),", "\n").replace("(", "").replace(",", ":").replace("[", " ").replace(")", " ").strip("[]")
