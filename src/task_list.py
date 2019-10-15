from src.main_class import MainClass


class TaskList(MainClass):
    def __init__(self, task):
        super().__init__()
        self.tasks = dict()
        for i in task:
            self.add_task(i)

    def __str__(self):
        # return str({u.name for u in self.tasks.values()})
        display = ''
        for i, j in enumerate([r.name for r in self.tasks.values()], start=1):
            display += str(i) + ': ' + str(j) + '\n'
        return display

    def add_task(self, task):
        self.tasks[task.uid] = task

    def remove_task(self, task):
        del self.tasks[task.uid]

    def get_all_task(self):
        a = ''
        for task in self.tasks.values():
            a += ''.join(str(task) + '\n')
        return a

    def sort_priority_task(self):
        sorted_task_list = [task[1] for task in sorted(self.tasks.items(), key=lambda x: x[1].priority)]
        k = ''
        for task in sorted_task_list:
            k += ''.join(str(task) + '\n')
        return k

    def get_one_task(self, uid):
        return self.tasks[uid]
