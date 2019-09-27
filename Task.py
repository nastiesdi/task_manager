from Dev import Dev
import hashlib


class Task:
    def __init__(self, name_task, priority_task, project_for_task=None, task_executor=None):
        self.name_task = name_task
        self.task_executor = task_executor
        if task_executor is not None:
            self.status_task = "Accepted"
        else:
            self.status_task = "Unasigned"
        self.project_for_task = project_for_task
        self.priority_task = priority_task
        self.uid = hashlib.sha224(bytes(str(self), 'utf-8')).hexdigest()[:10]
        #if task_executor == Dev.email:
        #    Dev().add_task(Task())

    def __str__(self):
        return (f'Task name: {self.name_task}. Executor {self.task_executor}. Status {self.status_task}.'
                f'Project {self.project_for_task}.Priority {self.priority_task}.')

    def delete_task(self, name_task):
        pass

    def sort_task_use_priority(self):
        pass

    def print_tasks_for_project(self):
        pass

    def add_executor_for_task(self, task_executor):
        self.task_executor = task_executor  # тут нужно проверить есть ли такой разработчик, и после того как мы
        # выводим какой-то таск, выводится вся инфа о разрабе, нужно только название, а так добавление работает!!

    def change_status_task(self, new_status):
        if new_status == 'Started' or new_status == 'Completed':
            self.status_task = new_status  # Super, rabotaet
        else:
            return print ("This status is not defined")

    def change_priority_task(self, new_priority):
        if new_priority is int and 0<new_priority<6:
            self.priority_task = new_priority  # Super, rabotaet
        else:
            print('This priority is not valid')
