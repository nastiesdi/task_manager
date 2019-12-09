import argparse
import pickle
import os

from src.dev import Dev
from src.task import Task
from src.project import Project
from manager import Manager
from helpers.consts import STATUS_LIST, PRIORITY, FOLDER_NAME, FILE_NAME, LOG_FILE_NAME


def parse_args():
    '''
        Добавить везде нормальный хелр, чтобы было похоже на прод вариант
    :return:
    '''
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    reg_parser = subparsers.add_parser('reg_user', help='jjj')
    reg_parser.add_argument('-e', '--email', type=str, help='The email must match the mask aa@ja.ar')
    reg_parser.add_argument('-p', '--password', type=str, help='Password must contain from 5 to 25 characters, at least'
                                                               ' 1 character of upper case, lower case and number ')
    reg_parser.add_argument('-r', '--repeat_password', type=str, help='Password and repeat password must match')
    reg_parser.add_argument('-f', '--first_name', type=str, help='First name must be between 2 and 15 latin characters')
    reg_parser.add_argument('-l', '--last_name', type=str, help='Last name must be between 2 and 15 latin characters')
    reg_parser.add_argument('-a', '--age', type=int, help='Age must be between 16 and 100')
    reg_parser.set_defaults(func=manager.registration)

    login_parser = subparsers.add_parser('login')
    login_parser.add_argument('-e', '--email', help='The entered email must be contained in the database')
    login_parser.add_argument('-p', '--password', help='Password must be valid for the entered email')
    login_parser.set_defaults(func=manager.login)
    # email, old_password, new_password, repeat_new_password)

    change_password = subparsers.add_parser('change_password')
    # change_password_pars.add_argument('-e', '--email')
    change_password.add_argument('-o', '--old_password', help='Old password must match current dev\'s password')
    change_password.add_argument('-n', '--new_password', help='Password must contain from 5 to 25 characters, at'
                                                              ' least 1 character of upper case, lower case and number')
    change_password.add_argument('-r', '--repeat_new_password', help='Password and repeat password must match')
    change_password.set_defaults(func=manager.change_password)

    create_task = subparsers.add_parser('create_task')
    create_task.add_argument('-n', '--name', help='Please, enter task\'s name')
    create_task.add_argument('-p', '--priority', choices=PRIORITY, help='Please, enter available priority')
    create_task.add_argument('-r', '--project', default=None,
                             help='Please, choose one of available project')
    create_task.add_argument('-e', '--executor', default=None)
    create_task.add_argument('-s', '--status', default='To do', choices=STATUS_LIST)
    create_task.add_argument('-t', '--sub_tasks', default=None, nargs='*', choices=manager.tasks,
                             help='If you wont you can add sub tasks to task ')
    create_task.set_defaults(func=manager.create_task)

    create_project = subparsers.add_parser('create_project')
    create_project.add_argument('-n', '--name')
    create_project.add_argument('-d', '--dev', nargs='*',
                                help='You can add developers to the project, just use their email.'
                                     ' You have to choose it from existing developers')
    create_project.set_defaults(func=manager.create_project)

    add_task = subparsers.add_parser('add_task')
    add_task.add_argument('-e', '--email', default=None)
    add_task.add_argument('-t', '--task_uid')
    add_task.set_defaults(func=manager.add_task_to_dev)

    add_dev_to_proj = subparsers.add_parser('add_dev_to_proj')
    add_dev_to_proj.add_argument('-e', '--email')
    add_dev_to_proj.add_argument('-p', '--project_uid')
    add_dev_to_proj.set_defaults(func=manager.add_dev_to_project)

    args = parser.parse_args()
    if 'func' in args:
        args.func(args)


def main():
    """В следубщей строке считываются аргументы из терминала"""
    parse_args()
    # manager.clean_project()

    """Сохранение изменений"""
    manager.save_devs()
    manager.save_current_dev()
    manager.save_projects()
    manager.save_tasks()

    """ Отображение всех девов, проектов и тасков"""""
    print('@@@@@@@@ developers @@@@@@@@@')
    for one in manager.developers.values():
        print(one)
        # print(one.email + '   ' + str(one.projects) + '    ' + str(one.all_tasks))
    print('\n@@@@@@@@@@@ projects @@@@@@@@@@@@')
    for one in manager.projects.values():
        print(str(one.name) + '   ' + str(one.dev) + '  ' + str(one.task) + '   ' + one.uid)
    print('\n@@@@@@@@@@@ tasks @@@@@@@@@@@@')
    for one in manager.tasks.values():
        print(str(one.name) + '  ' + str(one.project) + '  ' + (str(one.executor.email) if one.executor else '@@@') + '  ' + str(one.uid) +
              'sub tasks: ' + str(one.sub_tasks))


if __name__ == '__main__':
    manager = Manager(database_folder=FOLDER_NAME['data'], users_file=FILE_NAME['devs'],
                      cur_user_file=FILE_NAME['login'], project_file=FILE_NAME['projects'],
                      tasks_file=FILE_NAME['tasks'])
    # manager.clean_project()
    main()
