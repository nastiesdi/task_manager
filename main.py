#!/usr/bin/env python3.7

import argparse

from manager import Manager
from helpers.consts import STATUS_LIST, PRIORITY, FOLDER_NAME, FILE_NAME


def parse_args():
    parser = argparse.ArgumentParser(description='Great argument parser for Ad_como')

    subparsers = parser.add_subparsers(help='Sub-command help')

    developer_parser = subparsers.add_parser('developer', help='Do smth with developer')

    developer_subparsers = developer_parser.add_subparsers(help='sub-command help')

    register_parser = developer_subparsers.add_parser('register', help='For register new developer')
    register_parser.add_argument('-e', '--email', type=str, help='The email must match the mask aa@ja.ar',
                                 required=True)
    register_parser.add_argument('-p', '--password', type=str,
                                 help='Password must contain from 5 to 25 characters, min 1 character of upper case,'
                                      ' lower case and number ')
    register_parser.add_argument('-r', '--repeat_password', type=str, required=True,
                                 help='Password and repeat password must match')
    register_parser.add_argument('-f', '--first_name', type=str, required=True,
                                 help='First name must be between 2 and 15 latin characters')
    register_parser.add_argument('-l', '--last_name', type=str, required=True,
                                 help='Last name must be between 2 and 15 latin characters')
    register_parser.add_argument('-a', '--age', type=int, required=True, help='Age must be between 16 and 100')
    register_parser.set_defaults(func=manager.registration)

    login_parser = developer_subparsers.add_parser('login', help='Login user')
    login_parser.add_argument('-e', '--email', choices=manager.developers, required=True,
                              help='The entered email must be contained in the database')
    login_parser.add_argument('-p', '--password', required=True, help='Password must be valid for the entered email')
    login_parser.set_defaults(func=manager.login)

    change_password = developer_subparsers.add_parser('change_password', help='Change user password')
    change_password.add_argument('-o', '--old_password', required=True,
                                 help='Old password must match current dev\'s password')
    change_password.add_argument('-n', '--new_password', required=True,
                                 help='Password must contain from 5 to 25 characters, at least 1 character of upper'
                                      ' case, lower case and number')
    change_password.add_argument('-r', '--repeat_new_password',required=True,
                                 help='Password and new password must match')
    change_password.set_defaults(func=manager.change_password)

    show_devs = developer_subparsers.add_parser('all', help='Show all developers')
    show_devs.set_defaults(func=manager.show_all_devs)

    task_parser = developer_subparsers.add_parser('tasks', help='Do smth with developer')

    tasks_subparsers = task_parser.add_subparsers(help='sub-command help')

    remove_task = tasks_subparsers.add_parser('remove', help='Remove tasks from curent dev')
    remove_task.add_argument('-u', '--uid', required=True, help='Input uid for one or several tasks')
    remove_task.set_defaults(func=manager.remove_task_from_cur_dev)



    sort_dev_task_priority = tasks_subparsers.add_parser('priority', help='Show sorted task by priority')
    sort_dev_task_priority.add_argument('-e', '--email', required=True, help='Choose one of developers')
    sort_dev_task_priority.set_defaults(func=manager.sort_dev_tasks_priority)

    set_status_parser = tasks_subparsers.add_parser('set', help='set status')

    set_status_subparsers = set_status_parser.add_subparsers(help='sub-command help')

    change_status_on_in_progress = set_status_subparsers.add_parser('progress', help='Set status "in progress"')
    change_status_on_in_progress.add_argument('-e', '--email', choices=manager.developers, required=True,
                                              help='Choose one of developers')
    change_status_on_in_progress.add_argument('-u', '--uid', choices=manager.tasks, help='Please, choose one of tasks',
                                              required=True)
    change_status_on_in_progress.set_defaults(func=manager.set_status_in_progress)

    change_status_on_resolve = set_status_subparsers.add_parser('resolve', help='Set status "on resolve"')
    change_status_on_resolve.add_argument('-e', '--email', choices=manager.developers, required=True,
                                          help='Choose one of developers')
    change_status_on_resolve.add_argument('-u', '--uid', choices=manager.tasks, help='Please, choose one of tasks',
                                          required=True)
    change_status_on_resolve.set_defaults(func=manager.set_status_resolve)

    change_status_done = set_status_subparsers.add_parser('done', help='Set status "done"')
    change_status_done.add_argument('-e', '--email', choices=manager.developers, required=True,
                                    help='Choose one of developers')
    change_status_done.add_argument('-u', '--uid', choices=manager.tasks, help='Choose one tasks', required=True)
    change_status_done.set_defaults(func=manager.set_status_done)

    change_status_to_do = set_status_subparsers.add_parser('do', help='Set status "to_do"')
    change_status_to_do.add_argument('-e', '--email', choices=manager.developers, required=True,
                                     help='Choose one of developers')
    change_status_to_do.add_argument('-u', '--uid', choices=manager.tasks, help='Choose task', required=True)
    change_status_to_do.set_defaults(func=manager.set_status_to_do)

    show_task_parser = tasks_subparsers.add_parser('show', help='Do smth with developer')

    show_tasks_subparsers = show_task_parser.add_subparsers(help='sub-command help')

    show_devs_tasks = show_tasks_subparsers.add_parser('all', help='Show all dews task')
    show_devs_tasks.add_argument('-e', '--executor', choices=manager.developers, required=True,
                                 help='Choose one of developers')
    show_devs_tasks.set_defaults(func=manager.show_devs_tasks)

    show_tasks_with_status = show_tasks_subparsers.add_parser('status', help='Show tasks with chosen status ')
    show_tasks_with_status.add_argument('-e', '--executor', required=True, choices=manager.developers,
                                        help='Choose one of developers')
    show_tasks_with_status.add_argument('-s', '--status', required=True, choices=STATUS_LIST)
    show_tasks_with_status.set_defaults(func=manager.show_devs_tasks_with_status)

    show_tasks_with_priority = show_tasks_subparsers.add_parser('priority', help='Show tasks with chosen status ')
    show_tasks_with_priority.add_argument('-e', '--executor', required=True, choices=manager.developers,
                                          help='Choose one of developers')
    show_tasks_with_priority.add_argument('-p', '--priority', choices=PRIORITY, required=True,
                                          help='Please, enter available priority')
    show_tasks_with_priority.set_defaults(func=manager.show_tasks_with_priority)

    create_task = tasks_subparsers.add_parser('create', help='Create task ')
    create_task.add_argument('-n', '--name', help='Please, enter task\'s name', required=True)
    create_task.add_argument('-p', '--priority', choices=PRIORITY, required=True, help='Enter available priority')
    create_task.add_argument('-r', '--project', default=None, choices=manager.projects,
                             help='Please, choose one of available project')
    create_task.add_argument('-e', '--executor', required=True, choices=manager.developers)
    create_task.add_argument('-s', '--status', default='to_do', choices=STATUS_LIST)
    create_task.add_argument('-t', '--sub_tasks', default=None, nargs='*', choices=manager.tasks,
                             help='If you wont you can add sub tasks to task ')
    create_task.set_defaults(func=manager.create_task)

    change_task = tasks_subparsers.add_parser('change', help='Change task ')
    change_task.add_argument('-u', '--uid', choices=manager.tasks, help='Please, choose one of tasks', required=True)
    change_task.add_argument('-e', '--executor', choices=manager.developers, help='Choose one of developers')
    change_task.add_argument('-r', '--project', choices=manager.projects, help='Choose one of projects')
    change_task.add_argument('-p', '--priority', choices=PRIORITY, help='Please, enter new priority')
    change_task.add_argument('-t', '--sub_tasks', default=None, nargs='*', choices=manager.tasks,
                             help='If you wont you can add sub tasks to task ')
    change_task.add_argument('-s', '--status', choices=STATUS_LIST)
    change_task.set_defaults(func=manager.change_task)

    add_task = tasks_subparsers.add_parser('add', help='Add task to developer')
    add_task.add_argument('-e', '--email', required=True, choices=manager.developers, help='Choose one of developers')
    add_task.add_argument('-u', '--uid', required=True, choices=manager.tasks, help='Please, choose one of tasks')
    add_task.set_defaults(func=manager.add_task_to_dev)

    project_parser = subparsers.add_parser('project', help='Do smth with project')

    project_subparsers = project_parser.add_subparsers(help='sub-command help')

    create_project = project_subparsers.add_parser('create', help='Create project')
    create_project.add_argument('-n', '--name', required=True, help='Input project name')
    create_project.add_argument('-d', '--dev', nargs='*', choices=manager.developers,
                                help='You can add developers to the project, just use their email.'
                                     ' You have to choose it from existing developers')
    create_project.add_argument('-u', '--uid', choices=manager.tasks, nargs='*', help='Please, input project\'s task')
    create_project.set_defaults(func=manager.create_project)

    show_project = project_subparsers.add_parser('show', help='Show all projects')
    show_project.set_defaults(func=manager.show_all_project)

    show_project_tasks = project_subparsers.add_parser('show_with_task', help='Show all task projects')
    show_project_tasks.set_defaults(func=manager.show_all_task_for_project)

    rename_project = project_subparsers.add_parser('rename', help='Change name project')
    rename_project.add_argument('-u', '--proj_uid', required=True, choices=manager.projects,
                                help='Input uid chosen project')
    rename_project.add_argument('-n', '--new_name', required=True, help='Input new project name')
    rename_project.set_defaults(func=manager.rename_project)

    project_add_parser = project_subparsers.add_parser('add', help='Do smth with project')

    project_add_subparsers = project_add_parser.add_subparsers(help='sub-command help')

    add_dev_to_proj = project_add_subparsers.add_parser('dev', help='Add developer to project')
    add_dev_to_proj.add_argument('-e', '--email', required=True, choices=manager.developers,
                                 help='Choose one of developers')
    add_dev_to_proj.add_argument('-p', '--project_uid', choices=manager.projects, required=True,
                                 help='Choose one of project')
    add_dev_to_proj.set_defaults(func=manager.add_dev_to_project)

    add_task = project_add_subparsers.add_parser('task', help='Add task to project')
    add_task.add_argument('-e', '--email', required=True, choices=manager.developers, help='Choose one of developers')
    add_task.add_argument('-t', '--task_uid', choices=manager.tasks, required=True, help='Chose one of tasks')
    add_task.set_defaults(func=manager.add_task_to_dev)

    task_parser = subparsers.add_parser('tasks', help='Do smth with tasks')

    task_subparsers = task_parser.add_subparsers(help='sub-command help')

    create_task_without_dev = task_subparsers.add_parser('create', help='Create task')
    create_task_without_dev.add_argument('-n', '--name', help='Please, enter task\'s name', required=True)
    create_task_without_dev.add_argument('-p', '--priority', choices=PRIORITY, required=True,
                                         help='Enter available priority')
    create_task_without_dev.add_argument('-r', '--project', default=None, choices=manager.projects,
                                         help='Please, choose one of available project')
    create_task_without_dev.add_argument('-e', '--executor', choices=manager.developers, help='Chose developer')
    create_task_without_dev.add_argument('-s', '--status', default='to_do', choices=STATUS_LIST, help='Choose status')
    create_task_without_dev.add_argument('-t', '--sub_tasks', default=None, nargs='*', choices=manager.tasks,
                                         help='If you wont you can add sub tasks to task ')
    create_task_without_dev.set_defaults(func=manager.create_task)

    show_all_task = task_subparsers.add_parser('all', help='Show all task')
    show_all_task.set_defaults(func=manager.show_all_task)

    show_sub_task = task_subparsers.add_parser('sub_task', help='Show full info tasks')
    show_sub_task.add_argument('-t', '--task_uid', choices=manager.tasks, required=True, help='Choose one of tasks')
    show_sub_task.set_defaults(func=manager.show_subtask_for_task)

    add_subtask = task_subparsers.add_parser('add_subtask', help='Add sub task to task')
    add_subtask.add_argument('-t', '--task_uid', choices=manager.tasks, help='Chose one of tasks')
    add_subtask.add_argument('-s', '--sub_task_uid', choices=manager.tasks, help='Chose one of tasks')
    add_subtask.set_defaults(func=manager.add_sub_task)

    change_tasks = task_subparsers.add_parser('change', help='Change task ')
    change_tasks.add_argument('-u', '--uid', choices=manager.tasks, help='Please, choose one of tasks', required=True)
    change_tasks.add_argument('-e', '--executor', choices=manager.developers, help='Choose one of developers')
    change_tasks.add_argument('-r', '--project', choices=manager.projects, help='Choose one of projects')
    change_tasks.add_argument('-p', '--priority', choices=PRIORITY, help='Please, enter new priority')
    change_tasks.add_argument('-t', '--sub_tasks', default=None, nargs='*', choices=manager.tasks,
                              help='If you wont you can add sub tasks to task ')
    change_tasks.add_argument('-s', '--status', choices=STATUS_LIST)
    change_tasks.set_defaults(func=manager.change_task)

    args = parser.parse_args()
    if 'func' in args:
        args.func(args)


def main():
    """В следубщей строке считываются аргументы из терминала"""
    parse_args()

    """Сохранение изменений"""
    manager.save_devs()
    manager.save_current_dev()
    manager.save_projects()
    manager.save_tasks()


if __name__ == '__main__':
    manager = Manager(database_folder=FOLDER_NAME['data'], users_file=FILE_NAME['devs'],
                      cur_user_file=FILE_NAME['login'], project_file=FILE_NAME['projects'],
                      tasks_file=FILE_NAME['tasks'])
    main()
