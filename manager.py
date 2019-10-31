import argparse

from helpers.checker import is_valid_email, is_valid_password, is_valid_name
# from helpers.checker import
from src.dev import Dev
from src.task import Task
from src.project import Project
from helpers.consts import STATUS_LIST, PROJ_LIST, PRIORITY, DEV_LIST, TASK_LIST


def registration(email, password, repeat_password, first_name, last_name, age):
    dev = Dev(email=email,
              repeat_password=repeat_password,
              password=password,
              first_name=first_name,
              last_name=last_name,
              age=age)
    dev.add_to_dev_list()


class Manager:

    def __init__(self, dev=Dev):
        self.dev = dev

    # def registration(self, email, password, repeat_password, first_name, last_name, age):
    #     self.dev = Dev(email=email,
    #                    repeat_password=repeat_password,
    #                    password=password,
    #                    first_name=first_name,
    #                    last_name=last_name,
    #                    age=age)
    #     self.dev.add_to_dev_list()

    def login(self, email, password):
        current_password = ''
        for i in DEV_LIST.keys():
            if email == i:
                current_password = DEV_LIST[i]
                continue
            else:
                raise Exception('Email is not found')
        if password == current_password:
            return True
        else:
            raise Exception('Password is not correct')

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

    def show_subtask_for_task(self,task):
        pass

    def remove_subtask_task(self, task):
        pass

    def sort_dev_task_priority(self, dev):
        pass


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    reg_parser = subparsers.add_parser('reg_user')
    # reg_parser.add_argument('-s', '--self')
    reg_parser.add_argument('-e', '--email', type=str)
    reg_parser.add_argument('-p', '--password', type=str)
    reg_parser.add_argument('-rp', '--repeat_password', type=str)
    reg_parser.add_argument('-fn', '--first_name', type=str)
    reg_parser.add_argument('-ln', '--last_name', type=str)
    reg_parser.add_argument('-age', '--age', type=int)
    login_parser = subparsers.add_parser('login')
    login_parser.add_argument('-e', '--email')
    login_parser.add_argument('-p', '--password')
    args = parser.parse_args()
    reg_parser.set_defaults(funk=registration(**vars(args)))

    if 'funk' in args:
        print('@@@@@@')
        print(args)
        print('@@@@@@')
        args.func(args)


def main():
    dev1 = Dev(email='devSanya@mail.ru',
               password='123456difnastyalovesashaicultpassword',
               repeat_password='123456difnastyalovesashaicultpassword',
               first_name='Alexander',
               last_name='Gubin',
               age=21)
    dev1.add_to_dev_list()
    task1 = Task('create_database', 'Medium')
    task2 = Task('2nd task', 'low')
    task1.add_to_tasklist()
    project_mazad = Project('Mazad')
    project_mazad.add_task_to_project(task1)
    project_mazad.add_task_to_project(task2)
    project_mazad.add_to_proj_list()
    project_mazad.print_all_task()
    parse_args()
    print(DEV_LIST)


if __name__ == '__main__':
    main()
