
from src.main_class import MainClass
# from helpers.consts import TASK_LIST


class TaskList(MainClass):
    def __init__(self, tasks):
        super().__init__()
        self.tasks = dict()
        for task in tasks:
            self.add_task(task)

    def __str__(self):
        display = ''
        print(self.tasks.values())
        if self.tasks.values():
            for num, name in enumerate([task.name for task in self.tasks.values()], start=1):
                display += str(num) + ': ' + str(name) + '\n'
            return display

    def add_task(self, task):
        self.tasks[task] = task

    def remove_task(self, task):
        del self.tasks[task]

    def get_all_task(self):
        str_all_task = ''
        for task in self.tasks.values():
            str_all_task += ''.join(str(task) + '\n')
        return str_all_task

    def sort_priority_task(self):
        sorted_task_list = [task[1] for task in sorted(self.tasks.items(), key=lambda x: x[1].priority)]
        str_sort_task = ''
        for task in sorted_task_list:
            str_sort_task += ''.join(str(task.name) + ' -- task priority: ' + str(task.priority) + '\n')
        return str_sort_task

    def get_one_task(self, uid):
        return self.tasks[uid]
