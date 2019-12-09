import os

import jsonpickle

from logger import _get_logger
from src.dev import Dev
from src.task import Task
from src.project import Project
from helpers.consts import FOLDER_NAME, FILE_NAME, LOG_FILE_NAME


class Manager:
    def __init__(self, database_folder=None, users_file=None, cur_user_file=None, project_file=None, tasks_file=None,
                 log_file=None):
        self.developers = {}
        self.current_dev = None
        self.tasks = {}
        self.projects = {}
        if log_file:
            self.log_file = log_file
        else:
            self.log_file = f'{FOLDER_NAME["log"]}\{LOG_FILE_NAME["manager"]}'
        self.database_folder = database_folder if database_folder else FOLDER_NAME['data']
        self.users_file = users_file if users_file else FILE_NAME['devs']
        self.cur_user_file = cur_user_file if cur_user_file else FILE_NAME['login']
        self.project_file = project_file if project_file else FILE_NAME['projects']
        self.tasks_file = tasks_file if tasks_file else FILE_NAME['tasks']
        self.logger = _get_logger(self.log_file)
        self.load_tasks()
        self.load_project()
        self.load_current_dev()
        self.load_devs()

    def registration(self, args):
        if args.email not in self.developers:
            dev = Dev(email=args.email, repeat_password=args.repeat_password, password=args.password,
                      first_name=args.first_name, last_name=args.last_name, age=args.age)
            if dev:
                self.developers[dev.email] = dev
                self.logger.info(f'create Employee: {args.email}, First name: {args.first_name} ')
            else:
                self.logger.warning(f'Employee is not created: {args.email}, {args.first_name}, {args.repeat_password},'
                                    f'{args.password}, {args.first_name}, {args.last_name}, {args.age}')
        else:
            raise ValueError('This email is already in use')

    def login(self, args):
        if args.email in self.developers:
            if self.developers[args.email].check_password(args.password):
                self.current_dev = self.developers[args.email]
            else:
                self.logger.warning('User {args.email} try login use password - {args.password} ')
                raise ValueError('Input password is not correct')
        else:
            self.logger.warning(f'User cant register/ Input data: email - {args.email}, password - {args.password} ')
            raise ValueError('Developer doesn\'t exist')

    def change_password(self, args):
        if not self.current_dev:
            self.logger.warning(f'User is not loggin, current user ')
            raise ValueError('Please login!!!!!!!!!')
        self.current_dev.change_password(old_password=args.old_password, new_password=args.new_password,
                                         repeat_new_password=args.repeat_new_password)

    def create_task(self, args):
        task = Task(name=args.name,
                    priority=args.priority,
                    project=args.project if args.project else None,
                    executor=args.executor if args.executor else None,
                    status=args.status,
                    sub_tasks_uid=args.sub_tasks)
        self.tasks[task.uid] = task
        # if task.executor:
        #     self.developers[task.executor].all_task[task.uid] = task
        #     task.executor.add_task(task.uid)

    def create_project(self, args):
        project = Project(name=args.name, dev=args.dev)
        self.projects[project.uid] = project

    def change_project(self, args):
        pass

    def add_task_to_dev(self, args):
        pass
        # if self.current_dev:  # Перепиши чуть по лучше, условие
        #     if args.email:
        #         self.developers[args.email].add_task(args.task_uid)
        #         self.tasks[args.task_uid].change_task(task_executor=self.developers[args.email])
        #
        #     else:
        #         self.current_dev.add_task(args.task_uid)
        #         self.tasks[args.task_uid].change_task(task_executor=self.current_dev)
        # else:
        #     raise Exception('Please login')

    def add_dev_to_project(self, args):
        pass
        # # print(self.developers.keys())
        # self.projects[args.project_uid] = args
        # self.developers[args.email] = args

    def remove_task_from_dev(self, dev, task):
        pass

    def change_task(self, name, new_priority, new_project, new_executor, new_status):
        pass

    def show_all_dev_task(self, dev):
        pass

    def show_subtask_for_task(self, task):
        pass

    def remove_subtask_task(self, task):
        pass

    def sort_dev_task_priority(self, dev):
        pass

    def load_devs(self):
        if os.path.exists(os.path.join(self.database_folder, self.users_file)):
            with open(os.path.join(self.database_folder, self.users_file), 'r') as infile:
                self.developers = jsonpickle.decode(infile.readline())
                self.logger.info(f'Developers loaded: {self.developers}')
        else:
            self.logger.info(f'File is no exist ')

    def load_current_dev(self):
        if os.path.exists(os.path.join(self.database_folder, self.cur_user_file)):
            with open(os.path.join(self.database_folder, self.cur_user_file), 'r') as infile:
                self.current_dev = jsonpickle.decode(infile.readline())
                self.logger.info(f'Curent developer( {self.current_dev} )loaded ')
        else:
            self.logger.info(f'File is no exist ')

    def load_tasks(self):
        if os.path.exists(os.path.join(self.database_folder, self.tasks_file)):
            with open(os.path.join(self.database_folder, self.tasks_file), 'r') as infile:
                self.tasks = jsonpickle.decode(infile.readline())
                self.logger.info(f'Tasks loaded: {self.tasks} ')
        else:
            self.logger.info(f'File is no exist ')

    def load_project(self):
        if os.path.exists(os.path.join(self.database_folder, self.project_file)):
            with open(os.path.join(self.database_folder, self.project_file), 'r') as infile:
                self.projects = jsonpickle.decode(infile.readline())
                self.logger.info(f'Projects loaded: {self.projects}')
        else:
            self.logger.info(f'File is no exist ')

    def save_devs(self):
        with open(os.path.join(self.database_folder, self.users_file), 'tw') as outfile:
            outfile.write(jsonpickle.encode(self.developers))
            self.logger.info(f'Devs saved: {self.developers}')

    def save_current_dev(self):
        with open(os.path.join(self.database_folder, self.cur_user_file), 'tw') as outfile:
            outfile.write(jsonpickle.encode(self.current_dev))
            self.logger.info(f'login: {self.current_dev}')

    def save_tasks(self):
        with open(os.path.join(self.database_folder, self.tasks_file), 'tw') as outfile:
            outfile.write(jsonpickle.encode(self.tasks_file))
            self.logger.info(f'Tasks saved: {self.tasks}')

    def save_projects(self):
        with open(os.path.join(self.database_folder, self.project_file), 'tw') as outfile:
            outfile.write(jsonpickle.encode(self.project_file))
            self.logger.info(f'Projects saved: {self.projects}')

    def clean_project(self):
        self.tasks = {}
        self.developers = {}
        self.projects = {}
        self.current_dev = {}
# Тебе здесь еще пара методов нужны будут
# Прикинь какие
