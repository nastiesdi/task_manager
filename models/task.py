import time
import hashlib

from helpers.checker import check_priority


class Task:
    def __init__(self, name, priority, project=None, executor=None):
        self.name = name
        self.status = 'Unasigned'  # TODO: Rework status
        self.executor = executor
        self.created_at = time.strftime('%X, %x', time.localtime())  # TODO: MAINCLASS
        self.updated_at = 'not change'
        if executor:
            self.status = 'Accepted'
        self.project = project
        self.priority = priority
        self.uid = hashlib.sha224(bytes(str(self), 'utf-8')).hexdigest()[:10]

    def __str__(self):
        if self.executor is not None:
            return (f'1.Task name: {self.name}.\n2.Status: {self.status}.\n3.Executor: {self.executor.email}.\n'
                f'4.Priority {self.priority}.')
        return f'1.Task name: {self.name}.\n2.Status: {self.status}.\3.Priority {self.priority}.' #ЗАКОНЧИТЬ

    def show_full__info_task(self):
        if self.executor is not None:
            return (f'1.Task name: {self.name}.\n2.Executor: {self.executor.email}.\n3.Status: {self.status}.\n'
                    f'4.Project: {self.project.name_project}.\n5.Priority: {self.priority}.\n6.Created at: {self.created_at}.'
                    f'7. Updated at: {self.updated_at}')

    def delete_task(self, name_task):
        pass

    def print_tasks_for_project(self):
        pass

    def add_executor_for_task(self, dev):
        self.executor = dev

    def change_task(self, task_executor=None, new_priority=None, new_status=None):
        if task_executor:
            self.executor = task_executor  # тут нужно проверить есть ли такой разработчик, а так добавление работает!!
        if check_priority(new_priority):
            self.priority = new_priority  # Super, rabotaet
        self.updated_at = time.strftime('%X,%x', time.localtime())

    # TODO: Rework
    def change_status_task(self, new_status):
        if new_status == 'Started' or new_status == 'Completed':
            self.status = new_status  # Super, rabotaet
        else:
            return 'This status is not defined'

# TODO:
# 1. Name: Task name
# 2. Status task
# 3. Assigne
# 4. Priority               +
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
