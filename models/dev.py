import hashlib

from models.task_list import TaskList
from models.dev_list import DevList
from models.dev_list import devlist


class Dev:


    def __init__(self, email, password, first_name, second_name, age, task=[]):
        self.tasks = {}
        self.task_in_progress = TaskList({})
        self.task_resolve = TaskList({})
        self.task_done = TaskList({})
        self.email = email
        self.password = password
        self.first_name = first_name
        self.second_name = second_name
        self.age = age  # TODO Rework, list_of_tasks shuld be [to do, in progress, done, resolve, Default=To do]
        self.uid = hashlib.sha224(bytes(str(self), 'utf-8')).hexdigest()[:10]
        if task:
            if isinstance(task, list):
                for t in task:
                    self.tasks[t.uid] = t
             #       self.task_to_do.add_task(t)
            else:
                self.tasks[task.uid] = task
            #    self.task_to_do.add_task = task
        self.task_to_do = self.tasks.copy() # тут нужно вставить метод из дева: адд дев
        devlist.add_dev(self,dev=email)


    def __str__(self):
        output_asks = ' '
        for i in self.tasks.values():
            output_asks += str(i.name) + ', '
        return f'1.Developer mail: {self.email},\n2.First name:{self.first_name},'\
            f'\n3.Second name: {self.second_name},\n4.Age: {self.age},\n5.Tasks:{output_asks.rstrip(", ")} '

    def change_email(self, email):
        return self.email == email

    def check_password(self, my_password):
        return self.password == my_password

    def add_task(self, task):
        self.tasks[task.uid] = task
        self.task_to_do[task.uid] = task

    def remove_tasks(self, task_uid):
        if isinstance(task_uid, list):
            for t in task_uid:
                del self.tasks[t]
                if t in self.task_to_do:
                    del self.task_to_do[t]
                if t in self.task_in_progress:
                    del self.task_in_progress[t]
                if t in self.task_resolve:
                    del self.task_resolve[t]
                if t in self.task_done:
                    del self.task_done[t]
        else:
            del self.tasks[task_uid]
            del self.task_to_do[task_uid]
            if task_uid in self.task_to_do:
                del self.task_to_do[task_uid]
            if task_uid in self.task_in_progress:
                del self.task_in_progress[task_uid]
            if task_uid in self.task_resolve:
                del self.task_resolve[task_uid]
            if task_uid in self.task_done:
                del self.task_done[task_uid] # сделать с использованием мап, лямбда

    def show_all_dev_task(self):
        all_task = []
        for t in self.tasks.values():
            all_task.append(t.name)
        return print(all_task)

    def show_to_do_task(self):
        task_to_do_list = []
        for t in self.task_to_do.values():
            task_to_do_list.append(t.name)
        return print(task_to_do_list)

    def show_in_progress_task(self):
        task_in_progress_list = []
        for t in self.task_in_progress.values():
            task_in_progress_list.append(t.name)
        return print(task_in_progress_list)

    def show_resolve_task(self):
        resolve_task_list = []
        for t in self.task_resolve.values():
            resolve_task_list.append(t.name)
        return print(resolve_task_list)

    def show_done_task(self):
        done_task_list = []
        for t in self.task_done.values():
            done_task_list.append(t.name)
        return print(done_task_list)

    def set_task_in_progress(self, uid):
        pass #мне это нужно делать или вызывать функцию таск листа?
