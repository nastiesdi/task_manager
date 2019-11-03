import argparse
import pickle

from logger import LOGGER
from helpers.checker import is_valid_email, is_valid_password, is_valid_name
from src.dev import Dev
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

    def registration(self, args):
        # with open('login.pkl', 'rb') as infile:
        #     self = pickle.load(infile)
        if args.email not in self.developers:
            dev = Dev(email=args.email, repeat_password=args.repeat_password, password=args.password,
                      first_name=args.first_name, last_name=args.last_name, age=args.age)
            if dev:
                self.developers[dev.email] = dev
                with open('login.pkl', 'wb') as outfile:
                    pickle.dump(self, outfile, pickle.HIGHEST_PROTOCOL)
        else:
            raise ValueError('This email is already in use')
        LOGGER.info(f'create Employee: {args.email}, First name: {args.first_name} ')

    def login(self, args):
        if args.email in self.developers:
            if self.developers[args.email].check_password(args.password):
                self.current_dev = self.developers[args.email]
                with open('login.pkl', 'wb') as outfile:
                    pickle.dump(self, outfile, pickle.HIGHEST_PROTOCOL)
        else:
            LOGGER.warning(f'User cant register/ Input data: email - {args.email}, password - {args.password} ')
            raise KeyError('Developer doesn\'t exist')

    def change_password(self, email, old_password, repeat_old_password, new_password):
        pass

    def add_task_to_dev(self, email, task):
        pass

    def add_dev_to_project(self, email, project):
        pass

    def remove_task_from_dev(self, dev, task):
        pass

    def create_task(self, name, priority, project=None, executor=None, status='To do', sub_tasks=None):
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

# Тебе здесь еще пара методов нужны будут
# Прикинь какие
