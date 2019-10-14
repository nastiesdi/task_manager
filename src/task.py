import datetime
import hashlib

from helpers.consts import STATUS_LIST
from helpers.reformat import create_list_vision
from src.main_class import MainClass
from helpers.checker import check_priority


class Task(MainClass):
    def __init__(self, name, priority, project=None, executor=None, status='to do', sub_tasks=None):
        super().__init__()
        self.name = name
        self.executor = executor
        self.project = project
        self.priority = priority
        self.trek_time = datetime.timedelta()
        self.status = 'to do'
        self.sub_tasks = {}
        self.name_sub_tasks = []
        self.uid = hashlib.sha224(bytes(str(self), 'utf-8')).hexdigest()[:10]

    def __str__(self):
        if self.executor:
            return (f'1.Task name: {self.name}.\n2.Status - ?\n3.Executor: {self.executor.email}.\n'
                    f'4.Priority {self.priority}')
        return f'1.Task name: {self.name}.\n2.Status - ?\n3.Priority {self.priority}'

    def add_sub_tasks(self, new_sub_task):
        if isinstance(new_sub_task, list):
            for task in new_sub_task:
                self.sub_tasks[task.uid] = task
        else:
            self.sub_tasks[new_sub_task.uid] = new_sub_task

    def show_all_sub_tasks(self):
        self.name_sub_tasks = []
        for sub_task in self.sub_tasks.values():
            self.name_sub_tasks.append(sub_task.name)
            if sub_task.sub_tasks:
                sub_task.show_all_sub_tasks()
        # for sub_task in self.sub_tasks.values():
        print(f' - {self.name} : {self.name_sub_tasks}')

    def show_sub_tasks(self):
        self.name_sub_tasks = []
        for sub_task in self.sub_tasks.values():
            self.name_sub_tasks.append(sub_task.name)
        return f'Subtasks for {self.name} : {self.name_sub_tasks}'

    def remove_subtask(self, task):
        self.remove_all_subt_not_use(task)
        del self.sub_tasks[task.uid]

    def remove_all_subt_not_use(self, task):
        if task.sub_tasks:
            for i in list(task.sub_tasks.values()):
                del task.sub_tasks[i.uid]
                task.remove_all_subt_not_use(i)

    def show_full__info_task(self):
        n = [self.name, self.priority, self.created_at, self.updated_at, self.executor.email, self.project.name_project]
        b = ['name', 'priority', 'created_at', 'updated_at', 'executor', 'project']
        r = (list(zip(self.get_len_str(n), b)))
        return 'full info task: \n' + create_list_vision(str(list(zip(r, n))))

    def add_executor_for_task(self, dev):
        self.executor = dev
        self.update_time()

    def add_project_for_task(self, project):
        self.project = project
        self.update_time()

    def change_task(self, task_executor=None, new_priority=None):
        if task_executor:
            self.executor = task_executor  # тут нужно проверить есть ли такой разработчик, а так добавление работает!!
        if check_priority(new_priority):
            self.priority = new_priority

    def change_status_on_to_do(self):
        self.status = STATUS_LIST['to do']
        self.update_time()

    def change_status_on_in_progress(self):
        self.status = STATUS_LIST['in progress']
        self.update_time()

    def change_status_on_resolve(self):
        self.status = STATUS_LIST['resolve']

    def change_status_on_done(self):
        self.status = STATUS_LIST['done']


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
