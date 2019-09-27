from Task import Task


class Project:
    task = []

    def __init__(self, name_project, task=None, dev=None):
        self.name_project = name_project
        self.task = task
        self.dev = dev

    def __str__(self):
        return f'Name project: {self.name_project}'

    def add_task_to_project(self, task):
        self.task = Project.task
        if isinstance(task, list):
            for i in task:
                self.task.append(i)
        else:
            self.task.append(task)  # rabotaet

    def print_all_task(self):
        if Task.project_for_task == Project:
            return (f'{self.task_name}')
        pass
