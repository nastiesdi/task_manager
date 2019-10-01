from models.main_class import MainClass


class TaskList(MainClass):
    def __init__(self, task):
        super().__init__()
        self.tasks = dict()
        for i in task:
            self.tasks[i.uid] = i

    def __str__(self):
        for u in self.tasks.values():
            return u.name


    def add_task(self, task):
        self.tasks[task.uid] = task

    def remove_task(self, uid):
        del self.tasks[uid]

    def get_all_task(self):
        a = ''
        for task in self.tasks.values():
            a += ''.join(str(task) + '\n')
        return a

    def sort_priority_task(self):
        # a = []
        # for task in self.tasks.values():
        #     a.append(task)
        # sorted_tasks = sorted(a, key=operator.attrgetter('priority_task'))
        # a = ''
        # for task in sorted_tasks:
        #     a += ''.join(str(task) + '\n')
        # return a
        # print(list(self.tasks.values()).sort(key=lambda x: x.priority_task, reverse=True))
        sorted_task_list = [task[1] for task in sorted(self.tasks.items(), key=lambda x: x[1].priority_task)]
        k = ''
        for task in sorted_task_list:
            k += ''.join(str(task) + '\n')
        return k

    def get_one_task(self, uid):
        return self.tasks[uid]
