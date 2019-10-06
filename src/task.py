import time
import hashlib
from abc import ABC
from src.main_class import MainClass

from helpers.checker import check_priority


class Task(MainClass):
    def __init__(self, name, priority, project=None, executor=None, status='to do'):
        super().__init__()
        self.name = name
        self.executor = executor
        self.project = project
        self.priority = priority
        self.uid = hashlib.sha224(bytes(str(self), 'utf-8')).hexdigest()[:10]

    def __str__(self):
        if self.executor:
            return (f'1.Task name: {self.name}.\n2.Status - ?\n3.Executor: {self.executor.email}.\n'
                    f'4.Priority {self.priority}')
        return f'1.Task name: {self.name}.\n2.Status - ?\n3.Priority {self.priority}'

    def show_full__info_task(self):
        a = ''
        i = 5
        if self.executor:
            a = '\n' + str(i) + '.' + str(self.executor.email)
            i += 1
        if self.project:
            a += '\n' + str(i) + '.' + str(self.project.name_project)
        return print(f'1.Task name: {self.name}.\n2.Priority: {self.priority}.\n3.Created time: {self.created_at}.\n4'\
                     f'.Updated time: {self.updated_at}{a} ')

    def add_executor_for_task(self, dev):
        self.executor = dev

    def change_task(self, task_executor=None, new_priority=None):
        if task_executor:
            self.executor = task_executor  # тут нужно проверить есть ли такой разработчик, а так добавление работает!!
        if check_priority(new_priority):
            self.priority = new_priority  # Super, rabotaet

# TODO:

#     MANAGE PROJECT:
#   Name_project add -n 'Task' -p 6
#   Name_projecy project -n 'pr'
#   Name_projecy dev -n 'pr'
#   Name_project --all_tasks
#   Name_project --all_devs
#   Name_project dev registration -e 'Email' -u 'Username'
#   Name_project dev registration -e 'Tet' -u 'Test'
#   Name_project dev login -e 'Email' -u 'Username'
#   Name_project --all_tasks -s 'To do'
