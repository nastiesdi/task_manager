import datetime
import hashlib

from helpers.consts import STATUS_LIST, PRIORITY
from src.main_class import MainClass
from src.task_list import TaskList


class Task(MainClass):
    def __init__(self, name, priority, project=None, executor=None, status='To do', sub_tasks_uid=None):
        super().__init__()
        self.name = name
        self.executor = executor
        self.project = project
        self.trek_time = datetime.timedelta()
        self.status = status
        self.priority = PRIORITY[priority]
        self.status = STATUS_LIST[status]
        self.sub_tasks = {}
        self.name_sub_tasks = TaskList({})
        self.uid = hashlib.sha224(bytes(str(self), 'utf-8')).hexdigest()[:10]

    def __str__(self):
        task_info_list = []
        key_output_list = ['uid', 'name', 'status', 'priority', 'executor', 'trek_time']
        for key in key_output_list:
            if key in self.__dict__.keys() and self.__dict__[key]:
                task_info_list.append(str(key) + ': ' + str(self.__dict__[key]))
        display = 'Tasks info:\n'
        for num, info in enumerate(task_info_list, start=1):
            display += str(num) + '.' + str(info) + '\n'
        return display

    def add_sub_tasks(self, new_sub_task):
        if isinstance(new_sub_task, list):
            for task in new_sub_task:
                self.sub_tasks[task.uid] = task
        else:
            self.sub_tasks[new_sub_task.uid] = new_sub_task

    def show_sub_tasks(self):
        self.name_sub_tasks = []
        for sub_task in self.sub_tasks.values():
            self.name_sub_tasks.append(f' {sub_task.uid} - name: {sub_task.name}')
        return str(self.name_sub_tasks).strip("[]").replace("'", '')

    def remove_sub_task(self, task):
        self.remove_all_subt_not_use(task)
        del self.sub_tasks[task.uid]

    def remove_all_subt_not_use(self, task):
        if task.sub_tasks:
            for i in list(task.sub_tasks.values()):
                del task.sub_tasks[i.uid]
                task.remove_all_subt_not_use(i)

    def add_executor_for_task(self, dev):
        self.executor = dev
        self.update_time()

    def add_project_for_task(self, project):
        self.project = project
        self.update_time()

    def change_status_on_to_do(self):
        self.status = STATUS_LIST['to_do']
        self.update_time()

    def change_status_on_in_progress(self):
        self.status = STATUS_LIST['in_progress']
        self.update_time()

    def change_status_on_resolve(self):
        self.status = STATUS_LIST['resolve']
        self.update_time()

    def change_status_on_done(self):
        self.status = STATUS_LIST['done']
        self.update_time()
