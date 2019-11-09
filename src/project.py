import hashlib

from src.main_class import MainClass
from helpers.consts import PROJ_LIST, DEV_LIST


class Project(MainClass):
    def __init__(self, name, task=[], dev=None):
        super().__init__()
        self.name = name
        self.task = task
        self.uid = hashlib.sha224(bytes(str(self), 'utf-8')).hexdigest()[:10]
        self.dev = dev
        PROJ_LIST[self.uid] = self

    def __str__(self):
        return f'Name project: {self.name}'

    def add_task_to_project(self, task):
        if isinstance(task, list):
            for one in task:
                self.task.append(one)
        else:
            self.task.append(task)

    def print_all_task(self):
        display = 'All task:\n'
        for num, name in enumerate([r.name for r in self.task], start=1):
            display += str(num) + ': ' + str(name) + '\n'
        return display

    def add_to_proj_list(self):
        PROJ_LIST[self.name] = self

    def add_dev(self, email):
        self.dev.append(email)


