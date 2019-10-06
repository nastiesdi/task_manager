import hashlib

from src.task_list import TaskList
from src.dev_list import DevList


class Dev:
    def __init__(self, email, password, first_name, second_name, age, task=[]):
        self.dev_tasks = TaskList({})
        self.task_in_progress = TaskList({})
        self.task_resolve = TaskList({})
        self.task_done = TaskList({})
        self.task_to_do = TaskList({})
        self.email = email
        self.password = password
        self.first_name = first_name
        self.second_name = second_name
        self.age = age  # TODO Rework, list_of_tasks shuld be [to do, in progress, done, resolve, Default=To do]
        self.uid = hashlib.sha224(bytes(str(self), 'utf-8')).hexdigest()[:10]
        if task:
            if isinstance(task, list):
                for t in task:
                    self.dev_tasks.add_task(t)
                    self.task_to_do.add_task(t)
            else:
                self.dev_tasks.add_task(task)
                self.task_to_do.add_task(task)

    def __str__(self):
        output_tasks = ' '
        for i in self.dev_tasks.tasks.values():
            output_tasks += str(i.name) + ', '
        return f'1.Developer mail: {self.email},\n2.First name:{self.first_name},'\
            f'\n3.Second name: {self.second_name},\n4.Age: {self.age},\n5.Tasks:{output_tasks.rstrip(", ")}'

    def change_email(self, newemail):
        self.email = newemail

    def check_password(self, my_password):
        return self.password == my_password

    def add_task(self, task):
        if isinstance(task, list):
            for t in task:
                self.dev_tasks.add_task(t)
                self.task_to_do.add_task(t)
        else:
            self.dev_tasks.add_task(task)
            self.task_to_do.add_task(task)

    def remove_tasks(self, task_uid):
        if isinstance(task_uid, list):
            for t in task_uid:
                self.dev_tasks.remove_task(t)
                if t in self.task_to_do.tasks:
                    self.task_to_do.remove_task(t)
                if t in self.task_in_progress.tasks:
                    self.task_in_progress.remove_task(t)
                if t in self.task_resolve.tasks:
                    self.task_resolve.remove_task(t)
                if t in self.task_done.tasks:
                    self.task_done.remove_task(t)
        else:
            self.dev_tasks.remove_task(task_uid)
            if task_uid in self.task_to_do.tasks:
                self.task_to_do.remove_task(task_uid)
            if task_uid in self.task_in_progress.tasks:
                self.task_in_progress.remove_task(task_uid)
            if task_uid in self.task_resolve.tasks:
                self.task_resolve.remove_task(task_uid)
            if task_uid in self.task_done.tasks:
                self.task_done.remove_task(task_uid)

    def show_all_dev_task(self):
        return print({t.name for t in self.dev_tasks.tasks.values()})

    def show_to_do_task(self):
        return print({t.name for t in self.task_to_do.tasks.values()})

    def show_in_progress_task(self):
        return print({t.name for t in self.task_in_progress.tasks.values()})

    def show_resolve_task(self):
        return print({t.name for t in self.task_resolve.tasks.values()})

    def show_done_task(self):
        return print({t.name for t in self.task_done.tasks.values()})

    def set_task_in_progress(self, uid):
        self.remove_tasks(uid)
        self.add_task()
        pass #мне это нужно делать или вызывать функцию таск листа?
