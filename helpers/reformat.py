"""
Дорогие друзья!!!
Функция, следующая за этим текстом преобразует обычный список, в список, приятночитаемый. Уверяю вас, пользователи будут в восторге!
Попробуйте, и сами убедитесь=)
"""
def create_list_display(list_for_reformat):
    return str(list(enumerate(list_for_reformat, start=1))).replace("'", "").replace("),", "\n").replace("(", "").replace(",", ":").replace("[", " ").replace(")", " ").strip("[]")
