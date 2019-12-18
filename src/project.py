import hashlib

from src.task_list import TaskList

from src.main_class import MainClass


class Project(MainClass):
    def __init__(self, name, dev=None, tasks=None):
        super().__init__()
        self.name = name
        self.tasks = TaskList({})
        print(tasks)
        if tasks:
            self.tasks.add_task(tasks)
        self.uid = hashlib.sha224(bytes(str(self), 'utf-8')).hexdigest()[:10]
        self.dev = dev

    def __str__(self):
        task_info_list = []
        key_output_list = ['uid', 'name']
        for key in key_output_list:
            if key in self.__dict__.keys() and self.__dict__[key]:
                task_info_list.append(str(key) + ': ' + str(self.__dict__[key]))
        display = 'Project:\n'
        for num, info in enumerate(task_info_list, start=1):
            display += str(num) + '.' + str(info) + '\n'
        return display

    def add_task(self, task):
        if isinstance(task, list):
            for one in task:
                self.tasks.add_task(one)
        else:
            self.tasks.add_task(task)

    def rename(self, new_name):
        self.name = new_name
        return self.name

    def print_all_task(self):
        display = f'All task for project {self.name}:\n'
        for num, name in enumerate([r.name for r in self.tasks.tasks.values()], start=1):
            display += str(num) + ': ' + str(name) + '\n'
        print(display)

    def add_dev(self, email):
        self.dev.append(email)


