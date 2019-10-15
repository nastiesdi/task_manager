import hashlib

from src.task_list import TaskList
from src.main_class import MainClass


class Dev(MainClass):
    def __init__(self, email, password, first_name, last_name, age, task=[]):
        super().__init__()
        self.all_tasks = TaskList({})
        self.task_in_progress = TaskList({})
        self.task_resolve = TaskList({})
        self.task_done = TaskList({})
        self.task_to_do = TaskList({})
        self.email = email
        self.password = password
        self.first_name = first_name
        self.second_name = last_name
        self.age = age
        self.uid = hashlib.sha224(bytes(str(self), 'utf-8')).hexdigest()[:10]
        if task:
            if isinstance(task, list):
                for t in task:
                    self.all_tasks.add_task(t)
                    self.task_to_do.add_task(t)
            else:
                self.all_tasks.add_task(task)
                self.task_to_do.add_task(task)

    def __str__(self):
        output_tasks = ' '
        for i in self.all_tasks.tasks.values():
            output_tasks += str(i.name) + ', '
        return f'1.Developer mail: {self.email},\n2.First name:{self.first_name},' \
               f'\n3.Second name: {self.second_name},\n4.Age: {self.age},\n5.Tasks:{str(self.all_tasks).strip("{}")}'

    def change_email(self, new_email):
        self.email = new_email

    def check_password(self, my_password):
        return self.password == my_password

    def change_password(self, old_password, new_password):
        if self.check_password(old_password):
            self.password = new_password
        else:
            print('Old password is incorrect')

    def add_task(self, task):
        if isinstance(task, list):
            for t in task:
                self.all_tasks.add_task(t)
                self.task_to_do.add_task(t)
        else:
            self.all_tasks.add_task(task)
            self.task_to_do.add_task(task)

    def remove_task_absolutly(self, task):
        self.remove_tasks(task)
        self.all_tasks.remove_task(task)

    def remove_tasks(self, task):
        if isinstance(task, list):
            for t in task:
                if t.uid in self.task_to_do.tasks:
                    self.task_to_do.remove_task(t)
                if t.uid in self.task_in_progress.tasks:
                    self.task_in_progress.remove_task(t)
                if t.uid in self.task_resolve.tasks:
                    self.task_resolve.remove_task(t)
                if t.uid in self.task_done.tasks:
                    self.task_done.remove_task(t)
        else:
            if task.uid in self.task_to_do.tasks:
                self.task_to_do.remove_task(task)
            if task.uid in self.task_in_progress.tasks:
                self.task_in_progress.remove_task(task)
            if task.uid in self.task_resolve.tasks:
                self.task_resolve.remove_task(task)
            if task.uid in self.task_done.tasks:
                self.task_done.remove_task(task)

    def show_all_dev_task(self):
        return str([t.name for t in self.all_tasks.tasks.values()])

    def show_to_do_task(self):
        return str([t.name for t in self.task_to_do.tasks.values()])

    def show_in_progress_task(self):
        return str([t.name for t in self.task_in_progress.tasks.values()])

    def show_resolve_task(self):
        return str([t.name for t in self.task_resolve.tasks.values()])

    def show_done_task(self):
        return str([t.name for t in self.task_done.tasks.values()])

    def set_in_progress(self, task):
        task.change_status_on_in_progress()
        self.remove_tasks(task)
        self.task_in_progress.add_task(task)

    def set_resolve(self, task):
        if task in self.task_in_progress.tasks.values():
            temp_time = task.created_at if task.updated_at == 'Not changed' else task.updated_at
            task.change_status_on_to_do()
            task.trek_time += task.updated_at - temp_time
        self.remove_tasks(task)
        self.task_resolve.add_task(task)

    def set_done(self, task):
        self.remove_tasks(task)
        self.task_done.add_task(task)
        task.change_status_on_done()

    def set_to_do(self, task):
        if task in self.task_in_progress.tasks.values():
            temp_time = task.created_at if task.updated_at == 'Not changed' else task.updated_at
            task.change_status_on_to_do()
            task.trek_time += task.updated_at - temp_time
        self.remove_tasks(task)
        self.task_to_do.add_task(task)  # Добавить ексепшен
