import argparse
import pickle
import os

from logger import LOGGER
from helpers.checker import is_valid_email, is_valid_password, is_valid_name
from src.dev import Dev
from src.task import Task
from src.project import Project
from helpers.consts import STATUS_LIST, PROJ_LIST, PRIORITY, DEV_LIST, TASK_LIST

'''
    Ща раберешься с авторизацией и логином, прикрути сюда еще логгер, на эти два метода, все остальные по аалогии.
    Там на свое усмотрение логгируй то, что считаешь нужным. Крч покрыть все логрованием, настройки лоогера в отдельный 
    модуль вынесешь. Расширяй модуль consts.py, там будут дефолтные значения для названия файлов логгера, названия 
    файлов для сериализации девов, юзеров, тасков и проектов, если есть возможность не сделать из какого то значения 
    константу - делай - это хорошоая практика
'''


class Manager:
    def __init__(self):
        self.developers = {}
        self.current_dev = None
        self.tasks = {}
        self.projects = {}
        # for each in self.developers.keys():
        #     DEV_LIST[each] = self.developers[each]
        for each in self.projects.keys():
            PROJ_LIST[each] = self.projects[each]

    def add_const(self):
        for each in self.projects.keys():
            PROJ_LIST[each] = self.projects[each]
        for each in self.developers.keys():
            DEV_LIST[each] = self.developers[each]
        for each in self.tasks.keys():
            TASK_LIST[each] = self.tasks[each]

    def registration(self, args):
        if args.email not in self.developers:
            dev = Dev(email=args.email, repeat_password=args.repeat_password, password=args.password,
                      first_name=args.first_name, last_name=args.last_name, age=args.age)
            if dev:
                self.developers[dev.email] = dev
        else:
            raise ValueError('This email is already in use')
        LOGGER.info(f'create Employee: {args.email}, First name: {args.first_name} ')

    def login(self, args):
        if args.email in self.developers:
            if self.developers[args.email].check_password(args.password):
                self.current_dev = self.developers[args.email]
            else:
                raise ValueError('Input password is not correct')
        else:
            LOGGER.warning(f'User cant register/ Input data: email - {args.email}, password - {args.password} ')
            raise ValueError('Developer doesn\'t exist')

    def change_password(self, args):
        if self.current_dev:
            print('sssssss')
            print(self.current_dev.password)
            print(self.current_dev)
            self.current_dev.change_password(old_password=args.old_password, new_password=args.new_password,
                                             repeat_new_password=args.repeat_new_password)
        else:
            raise Exception('Please login')

    def create_task(self, args):
        task = Task(name=args.name, priority=args.priority,
                    project=self.projects[args.project] if args.project else None,
                    executor=self.developers[args.executor] if args.executor else None,
                    status=args.status, sub_tasks_uid=args.sub_tasks)
        self.tasks[task.uid] = task
        if task.executor:
            task.executor.add_task(task.uid)
        if task.project:
            task.project.add_task_to_project(task.uid)

    def create_project(self, args):
        project = Project(name=args.name, dev=args.dev)
        self.projects[project.uid] = project
        if args.dev:
            for one in args.dev:
                self.developers[one].add_project(project.uid)

    def change_project(self, args):
        pass

    def add_task_to_dev(self, args):
        if self.current_dev:  # Перепиши чуть по лучше, условие
            if args.email:
                self.developers[args.email].add_task(args.task_uid)
                TASK_LIST[args.task_uid].change_task(task_executor=self.developers[args.email])

            else:
                self.current_dev.add_task(args.task_uid)
                TASK_LIST[args.task_uid].change_task(task_executor=self.current_dev)
        else:
            raise Exception('Please login')

    def add_dev_to_project(self, args):
        print(self.developers.keys())
        self.projects[args.project_uid].add_dev(args.email)
        self.developers[args.email].add_project(args.project_uid)

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
        try:
            with open('searilization/devs.pkl', 'rb') as infile:
                self.developers = pickle.load(infile)
        except EOFError:
            return {}

    def load_current_dev(self):
        try:
            with open('searilization/session.pkl', 'rb') as infile:
                self.current_dev = pickle.load(infile)
        except EOFError:
            return {}

    def load_tasks(self):
        try:
            with open('searilization/tasks.pkl', 'rb') as infile:
                self.tasks = pickle.load(infile)
        except EOFError:
            return {}

    def load_project(self):
        try:
            with open('searilization/projects.pkl', 'rb') as infile:
                self.projects = pickle.load(infile)
        except EOFError:
            return {}


    def dump_devs(self):
        with open('searilization/devs.pkl', 'wb') as outfile:
            pickle.dump(self.developers, outfile, pickle.HIGHEST_PROTOCOL)

    def dump_current_dev(self):
        with open('searilization/session.pkl', 'wb') as outfile:
            pickle.dump(self.current_dev, outfile, pickle.HIGHEST_PROTOCOL)

    def dump_tasks(self):
        with open('searilization/tasks.pkl', 'wb') as outfile:
            pickle.dump(self.tasks, outfile, pickle.HIGHEST_PROTOCOL)

    def dump_projects(self):
        with open('searilization/projects.pkl', 'wb') as outfile:
            pickle.dump(self.projects, outfile, pickle.HIGHEST_PROTOCOL)

    def clean_project(self):
        self.tasks = {}
        self.developers = {}
        self.projects = {}
        self.current_dev = {}
# Тебе здесь еще пара методов нужны будут
# Прикинь какие
