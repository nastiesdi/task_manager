import hashlib

class Dev:
    task = []
    email = None

    def __init__(self, email, password, first_name, second_name, age, task=None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.uid = hashlib.sha224(bytes(str(self), 'utf-8')).hexdigest()[:10]
        if isinstance(task, list):
            self.task = []
            for i in task:
                self.task.append(i)
        else:
            self.task = task

    def __str__(self):
        return f'Developer mail: {self.email}, first name:{self.first_name}, second name: {self.second_name}, ' \
               f'age: {self.age} , {self.task}'

    def add_task(self, task):
        self.task = Dev.task
        if isinstance(task, list):
            for i in task:
                #               self.task.task_executor = Dev   (хочу чтобы автоматически в задачу записывалось имя
                #               испонителяБ тогда в конструкторе поставить ноне, и создавать задачу можно без указания
                #               исполнителя, так и с)   +++ add_executor_for_task (rabotaet=))
                self.task.append(i)
        else:
            self.task.append(task)


    def show_all_dev_task(self):
        if isinstance(self.task, list):
            for i in self.task:
                return




