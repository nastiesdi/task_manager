import argparse
import pickle
import jsonpickle
import json
import os

from logger import _get_logger
from helpers.checker import is_valid_email, is_valid_password, is_valid_name
from src.dev import Dev
from src.task import Task
from src.project import Project
# from helpers.consts import STATUS_LIST, PROJ_LIST, PRIORITY, DEV_LIST, TASK_LIST

'''
    Ща раберешься с авторизацией и логином, прикрути сюда еще логгер, на эти два метода, все остальные по аалогии.
    Там на свое усмотрение логгируй то, что считаешь нужным. Крч покрыть все логрованием, настройки лоогера в отдельный 
    модуль вынесешь. Расширяй модуль consts.py, там будут дефолтные значения для названия файлов логгера, названия 
    файлов для сериализации девов, юзеров, тасков и проектов, если есть возможность не сделать из какого то значения 
    константу - делай - это хорошоая практика
'''


class Manager:
    def __init__(self, database_folder=None, users_file=None, cur_user_file=None, project_folder=None, log_file=None):
        self.developers = {}
        self.current_dev = None
        self.tasks = {}
        self.projects = {}
        self.logger = _get_logger()
        if log_file:
            self.log_file = log_file
        else:
            self.log_file = 'log.log'
        self.load_tasks()
        self.load_project()
        self.load_current_dev()
        self.load_devs()


    def registration(self, args):
        if args.email not in self.developers:
            dev = Dev(email=args.email, repeat_password=args.repeat_password, password=args.password,
                      first_name=args.first_name, last_name=args.last_name, age=args.age)
            if dev:
                print("!!!!!!")
                print(type(dev))
                print(self.developers)
                print('!!!!!!!!!!')

                self.developers[dev.email] = dev
        else:
            raise ValueError('This email is already in use')
        self.logger.info(f'create Employee: {args.email}, First name: {args.first_name} ')

    def login(self, args):
        if args.email in self.developers:
            if self.developers[args.email].check_password(args.password):
                self.current_dev = self.developers[args.email]
            else:
                raise ValueError('Input password is not correct')
        else:
            # LOGGER.warning(f'User cant register/ Input data: email - {args.email}, password - {args.password} ')
            raise ValueError('Developer doesn\'t exist')

    def change_password(self, args):
        if not self.current_dev:
            raise ValueError('Tets')
        print('sssssss')
        print(self.current_dev.password)
        print(self.current_dev)
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
        if task.executor:
            self.developers[task.executor].all_task[task.uid] = task
            task.executor.add_task(task.uid)

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
        if os.path.exists('data/devs.json'):
            with open('data/devs.json', 'r') as infile:
                self.developers = jsonpickle.decode(infile.readline())

    def load_current_dev(self):
        if os.path.exists('data/session.json'):
            with open('data/session.json', 'r') as infile:
                self.current_dev = jsonpickle.decode(infile.readline())

    def load_tasks(self):
        if os.path.exists('data/tasks.json'):
            with open('data/tasks.json', 'r') as infile:
                self.tasks = jsonpickle.decode(infile.readline())

    def load_project(self):
        if os.path.exists('data/project.json'):
            with open('data/project.json', 'r') as infile:
                self.tasks = jsonpickle.decode(infile.readline())

    def save_devs(self):
        with open('data/devs.json', 'tw') as outfile:
            outfile.write(jsonpickle.encode(self.developers))


    def save_current_dev(self):
        with open('data/session.json', 'tw') as outfile:
            outfile.write(jsonpickle.encode(self.current_dev))

    def save_tasks(self):
        with open('data/tasks.json', 'tw') as outfile:
            outfile.write(jsonpickle.encode(self.tasks))

    def save_projects(self):
        with open('data/projects.json', 'tw') as outfile:
            outfile.write(jsonpickle.encode(self.projects))

    def clean_project(self):
        self.tasks = {}
        self.developers = {}
        self.projects = {}
        self.current_dev = {}
# Тебе здесь еще пара методов нужны будут
# Прикинь какие
