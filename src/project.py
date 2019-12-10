import hashlib

from src.task_list import TaskList

from src.main_class import MainClass


class Project(MainClass):
    def __init__(self, name, dev=None, tasks=None):
        super().__init__()
        self.name = name
        self.tasks = TaskList({})
        self.tasks.add_task(tasks)
        self.uid = hashlib.sha224(bytes(str(self), 'utf-8')).hexdigest()[:10]
        self.dev = dev

    def __str__(self):
        return f'Name project: {self.name}'

    def add_task(self, task):
        if isinstance(task, list):
            for one in task:
                self.tasks.add_task(one)
        else:
            self.tasks.add_task(task)

    def print_all_task(self):
        display = 'All task:\n'
        for num, name in enumerate([r.name for r in self.tasks.tasks.values()], start=1):
            display += str(num) + ': ' + str(name) + '\n'
        return display

    def add_dev(self, email):
        self.dev.append(email)


