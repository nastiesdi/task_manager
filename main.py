from time import sleep
import argparse
import sys

from src.dev import Dev
from src.dev_list import dev_list
from src.task import Task
from src.project import Project
from src.task_list import TaskList
from helpers.consts import STATUS_LIST, PROJ_LIST, PRIORITY, DEV_LIST, TASK_LIST
from helpers.checker import is_valid_email

# def main():
#
#     all_dev = DevList()
#     """Создание объектов"""
#     dev1 = Dev('devSanya@mail.ru', password='123456difnastyalovesashaicultpassword', first_name='Alexander', last_name='Gubin', age=21)
#     dev2 = Dev('devNastya@mail.ru', password='123412312', first_name='Nastya', last_name='Davydzenka', age=21)
#     dev3 = Dev('devDaha@mail.ru', password='123456', first_name='Daria', last_name='Shkuratova', age=21)
#     dev4 = Dev('devYulia@mail.ru', password='123456ss', first_name='Yulia', last_name='Filon', age=20)
#     dev5 = Dev('devLena@mail.ru', password='123456rrr', first_name='Alex', last_name='Kazackevich', age=26)
#     task1 = Task('create_database', 'Medium')
#     task2 = Task('add_field_task2', 'Medium')
#     task3 = Task('add_field_task3', 'Medium')
#     task4 = Task('fourth', 'Medium')
#     task5 = Task('five', 'Medium')
#     task6 = Task('Six', 'Medium')
#     task7 = Task('Seven', 'Medium')
#     task8 = Task('eignt', 'Medium')
#     task9 = Task('nine', 'Medium')
#     task10 = Task('ten', 'Medium')
#     print(task6.show_full_info_task())
#     project_mazad = Project('Mazad')
#     project_bosh = Project('Bosh')
#     task_list = TaskList([task2, task3, task4])
#     all_dev = dev_list
#     all_dev.add_dev([dev1, dev2, dev3, dev4, dev5])
#     print(str(all_dev) + '\n')
#     print('One of our developer\n' + str(dev1)+ '\n')
#     print('Changing email and password:\n 1.Use incorrect old password')
#     dev1.change_email('newemaildevSanya@gmail.com')
#     dev1.change_password('newpassword123', 'newpassword123')
#     print('email: ' + dev1.email)
#     print('password: ' + dev1.password)
#     print(' 2. Use correct old password')
#     dev1.change_password('123456', 'newpassword123')
#     print('new password is: ' + str(dev1.password))
#     print('\n Add task to dev')
#     dev1.add_task([task1, task2, task6, task7, task8, task9, task10])
#     print(dev1)
#     print('\n Remove devs task: "add_field_task2"')
#     dev1.remove_task_absolutely(task2)
#     print(dev1)
#     print('\nShow all dev tasks')
#     print(dev1.all_tasks)
#     print('\nShow all to do tasks')
#     print(dev1.task_to_do)
#     print('\nChange tasks status on in process\n To do tasks:')
#     dev1.set_in_progress(task7)
#     print(dev1.task_to_do)
#     print('Tasks in progress:')
#     print(dev1.task_in_progress)
#     sleep(1)
#     print('\nchange status task on to do ( time_track is changed)')
#     dev1.set_to_do(task7)
#     print(dev1.task_to_do)
#     print('Task ' + str(task7.name) + ' was in progress:')
#     print(task7.trek_time)
#     dev1.set_in_progress(task7)
#     sleep(2)
#     print('task ' + str(task7.name) + ' becomes resolve\n track time:')
#     dev1.set_resolve(task7)
#     print(task7.trek_time)
#     print('Sorted tasks ' + str(dev1.email) + ' :')
#     print(dev1.all_tasks.sort_priority_task())
#     print('Show all tasks sub_task')
#     print('@@@@@@@@@@@@@@@')
#     print(task1.sub_tasks)
#     task1.add_sub_tasks([task3, task4, task6])
#     task3.add_sub_tasks(task5)
#     print('@@@@@@@@@@@@@@@')
#     for task in task1.sub_tasks.values():
#         print(task.name)
#     print(task1.show_all_sub_tasks())
#     print('\nShow tasks sub_task "Create database"')
#     print(task1.show_sub_tasks())
#     task1.remove_subtask(task3)
#     print('\n Remove add_field_task3. All tasks: ')
#     print(task1.show_all_sub_tasks())
#     task1.add_executor_for_task(dev1)
#     task1.add_project_for_task(project_bosh)
#     print('\n' + str(task1.show_full_info_task()))
#     print('\nChange task\n')
#     task1.change_task(task_executor=dev2, new_priority='High')
#     print(task1.show_full_info_task())
#     all_devs = DevList()
#     all_devs.add_dev([dev3, dev1, dev2, dev4, dev5])
#     print(all_devs)
#     project_bosh.add_task_to_project([task1, task2, task3, task4])
#     print('\n' + str(project_bosh.print_all_task()))
#     print(task1)
#     print(dev2)


def create_new_project(args):
    project = Project(name_project=args.nameproject)
    project.add_to_proj_list()
    print(project)


def create_new_dev(args):
    developer = Dev(email=args.email,
                    password=args.password,
                    first_name=args.first_name,
                    last_name=args.last_name,
                    age=args.age)
    developer.add_to_dev_list()
    # print(DEV_LIST)


def create_task(args):
    task = Task(name=args.name,
                priority=args.priority,
                project=args.project,
                executor=args.executor,
                status=args.status
                # sub_tasks=args.sub_tasks
                )
    task.add_to_tasklist()
    # print(TASK_LIST)


def add_task_to_proj(args):
    task = TASK_LIST[args.nametask]
    project = PROJ_LIST[args.nameproject]
    project.add_task_to_project(task)
    print(project)

def print_task(args):
    project = PROJ_LIST[args.nameproject]
    project.print_all_task()
    # add visow

def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    proj_parser = subparsers.add_parser('proj')
    # add_task_parser = argparse.ArgumentParser(parents=[proj_parser])
    new_task_pareser = proj_parser.add_subparsers()
    add_task_parser = new_task_pareser.add_parser('taskpars')
    proj_parser.add_argument('-n', '--nameproject')
    proj_parser.set_defaults(func=create_new_project)
    add_task_parser.add_argument('-nt', '--nametask', choices=TASK_LIST)
    add_task_parser.set_defaults(func=add_task_to_proj)
    dev_parser = subparsers.add_parser('dev')
    dev_parser.add_argument('-e', '--email', type=str)
    dev_parser.add_argument('-p', '--password', type=str) #add check passwotd is valid
    dev_parser.add_argument('-fn', '--first_name', type=str)
    dev_parser.add_argument('-ln', '--last_name', type=str)
    dev_parser.add_argument('-a', '--age', type=int)
    dev_parser.set_defaults(func=create_new_dev)
    task_parser = subparsers.add_parser('task')
    task_parser.add_argument('-n', '--name', required=True)
    task_parser.add_argument('-p', '--priority', choices=PRIORITY)
    task_parser.add_argument('-pr', '--project', default=None, choices=PROJ_LIST)
    task_parser.add_argument('-ex', '--executor', default=None, choices=DEV_LIST)
    task_parser.add_argument('-s', '--status', default=STATUS_LIST['In progress'], choices=STATUS_LIST)
    # task_parser.add_argument('-sb', '--subtasks', default=None)
    task_parser.set_defaults(func=create_task)

    args = parser.parse_args()
    if 'func' in args:
        print('@@@@@@')
        print(args)
        print('@@@@@@')
        args.func(args)


def main():
    dev1 = Dev('devSanya@mail.ru', password='123456difnastyalovesashaicultpassword', first_name='Alexander',
               last_name='Gubin', age=21)
    dev1.add_to_dev_list()
    task1 = Task('create_database', 'Medium')
    task1.add_to_tasklist()
    project_mazad = Project('Mazad')
    project_mazad.add_to_proj_list()
    parse_args()


if __name__ == '__main__':
    main()
