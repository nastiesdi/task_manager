import datetime
import hashlib

from helpers.consts import STATUS_LIST, PRIORITY, TASK_LIST
from src.main_class import MainClass


class Task(MainClass):
    def __init__(self, name, priority, project=None, executor=None, status='To do', sub_tasks=None):
        super().__init__()
        self.name = name
        self.executor = executor
        self.project = project
        self.trek_time = datetime.timedelta() # track_time refactor
        self.status = status
        self.priority = PRIORITY[priority]
        self.track_time = datetime.timedelta()
        self.status = STATUS_LIST[status]
        self.sub_tasks = {}
        self.name_sub_tasks = []
        self.uid = hashlib.sha224(bytes(str(self), 'utf-8')).hexdigest()[:10]
        TASK_LIST[self.name] = self

    def __str__(self):
        task_info_list = []
        key_output_list = ['name', 'status', 'executor', 'priority']
        for key in self.__dict__.keys():
            if key == 'executor' and self.__dict__[key]:
                task_info_list.append(str(key) + ': ' + str(self.__dict__[key].email))
            elif key in key_output_list and self.__dict__[key]:
                task_info_list.append(str(key) + ': ' + str(self.__dict__[key]))
        display = 'Tasks info:\n'
        for num, info in enumerate(task_info_list, start=1):
            display += str(num) + '.' + str(info) + '\n'
        return display

    def add_to_tasklist(self):
        TASK_LIST[self.name] = self

    def add_sub_tasks(self, new_sub_task):
        if isinstance(new_sub_task, list):
            for task in new_sub_task:
                self.sub_tasks[task.uid] = task
        else:
            self.sub_tasks[new_sub_task.uid] = new_sub_task

    def show_all_sub_tasks(self):
        self.name_sub_tasks = []

        def add_sub_task(task):
            for sub_task in task.sub_tasks.values():
                self.name_sub_tasks.append(sub_task.name)  # uid везде нужны, ты получаешь везде все по юидам, должны быть единая система в проекте, ты не моежшь в одном месте получать инфу по юидам а в потом в другом месте взять и сделать ключом имя
                if sub_task.sub_tasks:
                    add_sub_task(sub_task)
        return self.name_sub_tasks

        # print(f' - {self.name}: ' + str(self.name_sub_tasks).strip("[]").replace("'", ''))
        # TODO
        # self.name_sub_tasks = []
        # for sub_task in self.sub_tasks.values():
        #     self.name_sub_tasks.append(sub_task.name)
        #     if sub_task.sub_tasks:
        #         sub_task.show_all_sub_tasks()
        # print(f' - {self.name}: ' + str(self.name_sub_tasks).strip("[]").replace("'", ''))

        # name_sub_tasks = []
        # name_sub = ''
        # for sub_task in self.sub_tasks.values():
        #     name_sub_tasks.append(sub_task.name)
        #     if sub_task.sub_tasks:
        #         sub_task.show_all_sub_tasks()
        #     name_sub += f' - {self.name}: ' + str(name_sub_tasks).strip("[]").replace("'", '')
        # return name_sub

    # Add with Sasha
    # tasks = []
    # def fill_tasks():
    #     for sub_task in self.sub_tasks:
    #         tasks

    def show_sub_tasks(self):
        self.name_sub_tasks = []
        for sub_task in self.sub_tasks.values():
            self.name_sub_tasks.append(sub_task.name)
        return str(self.name_sub_tasks).strip("[]").replace("'", '')

    def remove_subtask(self, task):
        self.remove_all_subt_not_use(task)
        del self.sub_tasks[task.uid]

    """
    Следующий метод используется как внутренний для другого, 
    отдельно использование не рекомендуется
    
    Если у тебя получилась такая ситуация, когда тебе нужно сделать какой либо метод приватный - знаит ты делаешь что то неправильно
    Нужно избавиться от этого
    """

    def remove_all_subt_not_use(self, task):
        if task.sub_tasks:
            for i in list(task.sub_tasks.values()):
                del task.sub_tasks[i.uid]
                task.remove_all_subt_not_use(i)
    '''
        Смысл этой гтуки был в том, что когда ты ыведешь инфу о таске, например, и у тебя вылетят юиды каких либо тасков 
        следом, например сабтасков и на, например, захотела унать инфу об этом сабтаске, ты скопировала этот юид из 
        терминала, скормила его этой функции и получила инфу, и так вообще с любым таском, сейчас так не раотает
        сейчс он привязан к конкретному таску
    '''
    def show_full_info_task(self):
        task_info_list = []
        for key in self.__dict__.keys():
            if key == 'executor' and self.__dict__[key]:
                task_info_list.append(str(key) + ': ' + str(self.__dict__[key].email))
            elif key != 'sub_tasks' and self.__dict__[key]:
                task_info_list.append(str(key) + ': ' + str(self.__dict__[key]))
        display = 'Full info tasks:\n'
        for i, j in enumerate(task_info_list, start=1):
            display += str(i) + '.' + str(j) + '\n'
        return display

    def add_executor_for_task(self, dev):
        self.executor = dev
        self.update_time()

    def add_project_for_task(self, project):
        self.project = project
        self.update_time()

    def change_task(self, task_executor=None, new_priority=None):
        if task_executor:
            self.executor = task_executor  # тут нужно проверить есть ли такой разработчик, а так добавление работает!! Решай вопрос
        self.priority = PRIORITY[new_priority]

    def change_status_on_to_do(self):
        self.status = STATUS_LIST['To do']
        self.update_time()

    def change_status_on_in_progress(self):
        self.status = STATUS_LIST['In progress']
        self.update_time()

    def change_status_on_resolve(self):
        self.status = STATUS_LIST['Resolve']
        self.update_time()

    def change_status_on_done(self):
        self.status = STATUS_LIST['Done']
        self.update_time()

# TODO:

#     MANAGE PROJECT:
#   Name_project add -n 'Task' -p 6
#   Name_projecy project -n 'pr'
#   Name_projecy dev -n 'pr'
#   Name_project --all_tasks
#   Name_project --all_devs
#   Name_project dev registration -e 'Email' -u 'Username'
#   Name_project dev registration -e 'Tet' -u 'Test'
#   Name_project dev login -e 'Email' -u 'Username'
#   Name_project --all_tasks -s 'To do'
