import os

import jsonpickle

from logger import _get_logger
from src.dev import Dev
from src.task import Task
from src.project import Project
from helpers.consts import FOLDER_NAME, FILE_NAME, LOG_FILE_NAME
from helpers.decorators import login_required

class Manager:
    def __init__(self, database_folder=None, users_file=None, cur_user_file=None, project_file=None, tasks_file=None,
                 log_folder=None, log_file=None):
        self.developers = {}
        self.current_dev = None
        self.tasks = {}
        self.projects = {}
        self.log_folder = log_folder if log_folder else FOLDER_NAME['log']
        self.log_file = log_file if log_file else LOG_FILE_NAME['manager']
        self.database_folder = database_folder if database_folder else FOLDER_NAME['data']
        self.users_file = users_file if users_file else FILE_NAME['devs']
        self.cur_user_file = cur_user_file if cur_user_file else FILE_NAME['login']
        self.project_file = project_file if project_file else FILE_NAME['projects']
        self.tasks_file = tasks_file if tasks_file else FILE_NAME['tasks']
        self.log_file = os.path.join(self.log_folder, self.log_file)
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
                self.logger.info(f'Developer {dev.uid} with email {dev.email} successfully created')
            else:
                self.logger.warning(f'Employee is not created: {args.email}, {args.first_name}, {args.repeat_password},'
                                    f'{args.password}, {args.first_name}, {args.last_name}, {args.age}')
        else:
            raise ValueError('This email is already in use')

    def login(self, args):
        if args.email in self.developers:
            if self.developers[args.email].check_password(args.password):
                self.current_dev = self.developers[args.email]
                self.logger.warning(f'User {args.email} login use password - {args.password} ')
            else:
                self.logger.warning(f'User {args.email} try login use password - {args.password} ')
                raise ValueError('Input password is not correct')
        else:
            self.logger.warning(f'User cant register/ Input data: email - {args.email}, password - {args.password} ')
            raise ValueError('Developer doesn\'t exist')

    @login_required
    def change_password(self, args):
        self.current_dev.change_password(old_password=args.old_password, new_password=args.new_password,
                                         repeat_new_password=args.repeat_new_password)
        self.developers[self.current_dev.email].change_password(old_password=args.old_password,
                                                                new_password=args.new_password,
                                                                repeat_new_password=args.repeat_new_password)
        self.logger.info(f'User {self.current_dev} with name {self.current_dev} change password on {args.new_password}')

    @login_required
    def show_all_devs(self, args):
        self.logger.info(f'user show all devs')
        for each in self.developers.values():
            print(each)

    @login_required
    def show_devs_tasks(self, args):
        self.logger.info(f'user show all devs')
        for each in self.tasks.values():
            if each.executor == args.executor:
                print(each)

    @login_required
    def show_devs_tasks_with_status(self, args):
        for each in self.tasks.values():
            if each.executor == args.executor and each.status == args.status:
                print(each)
        self.logger.info(f'user show devs tasks using status')

    @login_required
    def show_tasks_with_priority(self, args):
        for each in self.tasks.values():
            if each.executor == args.executor and each.status == args.priority:
                print(each)
        self.logger.info(f'user show devs tasks using priority')

    @login_required
    def sort_dev_tasks_priority(self, args):
        self.logger.info(f'user sort task by priority')
        print(self.developers[args.email].all_tasks.sort_priority_task())

    @login_required
    def create_task(self, args):
        task = Task(name=args.name,
                    priority=args.priority,
                    project=args.project if args.project else None,
                    executor=args.executor if args.executor else None,
                    status=args.status,
                    sub_tasks_uid=args.sub_tasks)
        self.tasks[task.uid] = task
        self.logger.info(f'Task {task.uid} with name {task.name} was created '
                         f'(project - {task.project}, executor - {task.executor}')
        if task.executor:
            self.developers[task.executor].add_task(task)
        if task.project:
            self.projects[task.project].add_task(task)

    @login_required
    def change_task(self, args):
        if args.executor:
            old_executor = self.tasks[args.uid].executor
            if old_executor:
                self.developers[old_executor].remove_tasks(args.uid)
            self.tasks[args.uid].executor = args.executor
            self.developers[args.executor].add_task(self.tasks[args.uid])
            self.logger.info(f'Executor for task {args.uid} is changed from {old_executor if old_executor else "None" } '
                             f'to {args.executor}')
        if args.project:
            old_project = self.tasks[args.uid].project
            if old_project:
                self.projects[old_project].tasks.remove_task(args.uid)
            self.projects[args.project].add_task(args.uid)
            self.tasks[args.uid].project = args.project
            self.logger.info(f'Project for task {args.uid} is changed from {old_project if old_project else "None"} '
                             f'to {args.project}')
        if args.priority:
            self.tasks[args.uid].priority = args.priority
            self.logger.info(f'Priority for task {args.uid} is changed to {args.priority}')
        if args.status:
            self.tasks[args.uid].status = args.status
            self.logger.info(f'Status for task {args.uid} is changed to {args.status}')

    @login_required
    def add_sub_task(self, args):
        old_subtasks = self.tasks[args.task_uid].sub_tasks
        self.tasks[args.task_uid].add_sub_tasks(self.tasks[args.sub_task_uid])
        self.logger.info(f'To task {args.task_uid} was add sub_task. Old_subtask -  {old_subtasks}'
                         f'New sub_tasks {self.tasks[args.task_uid].sub_tasks}')

    @login_required
    def set_status_in_progress(self, args):
        old_status = self.tasks[args.uid].status
        old_tracked_time = self.tasks[args.uid].trek_time
        self.developers[args.email].set_in_progress(self.tasks[args.uid])
        self.logger.info(f'Status for task {args.uid} is changed from {old_status} to {self.tasks[args.uid].status}'
                         f'old trecked time - {old_tracked_time}, new - {self.tasks[args.uid].trek_time}')

    @login_required
    def set_status_resolve(self, args):
        old_status = self.tasks[args.uid].status
        old_tracked_time = self.tasks[args.uid].trek_time
        self.developers[args.email].set_resolve(self.tasks[args.uid])
        self.logger.info(f'Status for task {args.uid} is changed from {old_status} to {self.tasks[args.uid].status}'
                         f' old trecked time - {old_tracked_time}, new - {self.tasks[args.uid].trek_time}')

    @login_required
    def set_status_done(self, args):
        old_status = self.tasks[args.uid].status
        old_tracked_time = self.tasks[args.uid].trek_time
        self.developers[args.email].set_done(self.tasks[args.uid])
        self.logger.info(f'Status for task {args.uid} is changed from {old_status} to {self.tasks[args.uid].status}'
                         f' old trecked time - {old_tracked_time}, new - {self.tasks[args.uid].trek_time}')

    @login_required
    def set_status_to_do(self, args):
        old_status = self.tasks[args.uid].status
        old_tracked_time = self.tasks[args.uid].trek_time
        self.developers[args.email].set_to_do(self.tasks[args.uid])
        self.logger.info(f'Status for task {args.uid} is changed from {old_status} to {self.tasks[args.uid].status}'
                         f' old trecked time - {old_tracked_time}, new - {self.tasks[args.uid].trek_time}')

    @login_required
    def create_project(self, args):
        project = Project(name=args.name, dev=args.dev)
        if args.uid:
            for each in args.uid:
                project.add_task(self.tasks[each])
        self.projects[project.uid] = project
        self.logger.info(f'Project {project.uid} with name {project.name} was created ')

    @login_required
    def show_all_task(self, args):
        for each in self.tasks.values():
            print(each)

    @login_required
    def show_all_project(self, args):
        for each in self.projects.values():
            print(each)

    @login_required
    def show_all_task_for_project(self, args):
        for each in self.projects.values():
            each.print_all_task()

    @login_required
    def rename_project(self, args):
        self.projects[args.proj_uid].rename(args.new_name)

    @login_required
    def add_task_to_dev(self, args):
        self.developers[args.email].add_task(self.tasks[args.uid])
        self.tasks[args.uid].executor = args.email
        self.logger.info(f'Task {args.uid} is added to {args.email}')

    @login_required
    def add_dev_to_project(self, args):
        self.projects[args.project_uid].dev = args.email
        self.developers[args.email] = args.project_uid
        self.logger.info(f'Task {args.uid} is added to project: {args.project_uid}')

    @login_required
    def remove_task_from_cur_dev(self, args):
        if args.uid not in self.current_dev.all_tasks.tasks:
            raise Exception(f'Curent user haven\'t task with uid {args.uid}')
        self.current_dev.remove_tasks(args.uid, is_deleted_at_all=True)
        self.developers[self.current_dev.email].remove_tasks(args.uid, is_deleted_at_all=True)
        self.tasks[args.uid].executor = None

    @login_required
    def show_subtask_for_task(self, args):
        self.logger.info(f'Show info about task {args.task_uid}: {self.tasks[args.task_uid]}')
        print(self.tasks[args.task_uid].show_sub_tasks())

    @login_required
    def remove_subtask(self, task_uid):
        parent_task = None
        for each in self.tasks.values():
            if task_uid in each.sub_tasks:
                parent_task = each
                break
        parent_task.remove_sub_task(task_uid)

    def load_devs(self):
        if os.path.exists(os.path.join(self.database_folder, self.users_file)):
            with open(os.path.join(self.database_folder, self.users_file), 'r') as infile:
                self.developers = jsonpickle.decode(infile.readline())
        else:
            self.logger.info(f'File {(os.path.join(self.database_folder, self.users_file))} is no exist ')

    def load_current_dev(self):
        if os.path.exists(os.path.join(self.database_folder, self.cur_user_file)):
            with open(os.path.join(self.database_folder, self.cur_user_file), 'r') as infile:
                self.current_dev = jsonpickle.decode(infile.readline())
        else:
            self.logger.info(f'File {(os.path.join(self.database_folder, self.cur_user_file))}is no exist ')

    def load_tasks(self):
        if os.path.exists(os.path.join(self.database_folder, self.tasks_file)):
            with open(os.path.join(self.database_folder, self.tasks_file), 'r') as infile:
                self.tasks = jsonpickle.decode(infile.readline())
        else:
            self.logger.info(f'File {os.path.join(self.database_folder, self.tasks_file)} is no exist ')

    def load_project(self):
        if os.path.exists(os.path.join(self.database_folder, self.project_file)):
            with open(os.path.join(self.database_folder, self.project_file), 'r') as infile:
                self.projects = jsonpickle.decode(infile.readline())
        else:
            self.logger.info(f'File {os.path.join(self.database_folder, self.project_file)} is no exist ')

    def save_devs(self):
        with open(os.path.join(self.database_folder, self.users_file), 'tw') as outfile:
            outfile.write(jsonpickle.encode(self.developers))

    def save_current_dev(self):
        with open(os.path.join(self.database_folder, self.cur_user_file), 'tw') as outfile:
            outfile.write(jsonpickle.encode(self.current_dev))

    def save_tasks(self):
        with open(os.path.join(self.database_folder, self.tasks_file), 'tw') as outfile:
            outfile.write(jsonpickle.encode(self.tasks))

    def save_projects(self):
        with open(os.path.join(self.database_folder, self.project_file), 'tw') as outfile:
            outfile.write(jsonpickle.encode(self.projects))
