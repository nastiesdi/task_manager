import hashlib

from logger import _get_logger
from src.task_list import TaskList
from src.main_class import MainClass
from helpers.checker import is_valid_email, is_valid_name, is_valid_password, is_valid_age
from helpers.consts import STATUS_LIST



# Юзменяемые типы не используй в аргументах
class Dev(MainClass):
    def __init__(self, email, password, repeat_password, first_name, last_name, age):
        """
        :param email: maska fff@hh.hh
        :param password: cdcdcddcdc
        :param repeat_password:
        :param first_name:
        :param last_name:
        :param age:
        :param task:
        """
        super().__init__()
        self.all_tasks = TaskList({})
        self.task_in_progress = TaskList({})
        self.task_resolve = TaskList({})
        self.task_done = TaskList({})
        self.task_to_do = TaskList({})
        self.projects = {}
        if is_valid_email(email):
            self.email = email
        else:
            raise Exception('Email is not valid')
        if is_valid_password(password):
            if password == repeat_password:
                self.password = password
            else:
                raise ValueError('Passwords are not match')
        else:
            raise Exception('Password is not valid')
        if is_valid_name(first_name):
            self.first_name = first_name
        else:
            raise ValueError('First name must be between 2 and 15 latin characters')
        if is_valid_name(last_name):
            self.last_name = last_name
        else:
            raise ValueError('Last name must be between 2 and 15 latin characters')
        if is_valid_age(age):
            self.age = age
        else:
            raise ValueError('Age must be between 16 and 100')
        self.uid = hashlib.sha224(bytes(str(self), 'utf-8')).hexdigest()[:10]
        # if tasks:
        #     if isinstance(tasks, list):
        #         for one in tasks: # for task in tasks?
        #             self.all_tasks.add_task(one)
        #             self.task_to_do.add_task(one)
        #     else:
        #        self.all_tasks.add_task(tasks)
        #     self.task_to_do.add_task(tasks)

    def __str__(self):
        task_info_list = []
        key_output_list = ['email', 'first_name', 'last_name', 'task', 'age']
        for key in key_output_list:
            if key in self.__dict__.keys() and self.__dict__[key]:
                task_info_list.append(str(key) + ': ' + str(self.__dict__[key]))
        display = 'Dev:\n'
        for i, j in enumerate(task_info_list, start=1):
            display += str(i) + '.' + str(j) + '\n'
        return display

    def check_password(self, my_password):
        return self.password == my_password

    def change_email(self, new_email):
        if is_valid_email(new_email):
            self.email = new_email
        else:
            raise ValueError('Email is not valid')

    def change_password(self, old_password, new_password, repeat_new_password):
        if is_valid_password(new_password):
            if self.password == old_password:
                if new_password == repeat_new_password:
                    self.password = new_password
                else:
                    raise ValueError('New password and repeat new password are not match')
            else:
                raise ValueError('Old passwords is not correct')
        else:
            raise ValueError('New password is not valid')

    def add_task(self, task):
        if isinstance(task, list):
            for one in task:
                self.all_tasks.add_task(one)
                self.task_to_do.add_task(one)
        else:
            self.all_tasks.add_task(task)
            self.task_to_do.add_task(task)

    def remove_tasks(self, task, is_deleted_at_all=False):
        if isinstance(task, list):
            for t in task:
                if t in self.task_to_do.tasks:
                    self.task_to_do.remove_task(t)
                if t in self.task_in_progress.tasks:
                    self.task_in_progress.remove_task(t)
                if t in self.task_resolve.tasks:
                    self.task_resolve.remove_task(t)
                if t in self.task_done.tasks:
                    self.task_done.remove_task(t)
        else:
            print(task)
            if task in self.task_to_do.tasks:
                self.task_to_do.remove_task(task)
            if task in self.task_in_progress.tasks:
                self.task_in_progress.remove_task(task)
            if task in self.task_resolve.tasks:
                self.task_resolve.remove_task(task)
            if task in self.task_done.tasks:
                self.task_done.remove_task(task)
        if is_deleted_at_all:
            self.all_tasks.remove_task(task)
            # del TASK_LIST[task.name]

    def set_in_progress(self, task):
        task.change_status_on_in_progress()
        self.remove_tasks(task)
        self.task_in_progress.add_task(task)

    def set_resolve(self, task):
        print(task.status)
        if task.status == 'in progress':
            print('@@@@@@@@@@@@@@@@@@@')
            temp_time = task.created_at if task.updated_at == 'Not changed' else task.updated_at
            print(task.created_at)
            print(task.updated_at)
            print(temp_time)
            task.trek_time += task.updated_at - temp_time
            print(task.trek_time)
        self.remove_tasks(task)
        task.change_status_on_resolve()
        self.task_resolve.add_task(task)

        ##reshim

    def set_done(self, task):
        self.remove_tasks(task)
        self.task_done.add_task(task)
        task.change_status_on_done()

    def set_to_do(self, task):
        if task.status == 'in progress':
            temp_time = task.created_at if task.updated_at == 'Not changed' else task.updated_at
            task.trek_time += task.updated_at - temp_time
        task.change_status_on_to_do()
        self.remove_tasks(task)
        self.task_to_do.add_task(task)
