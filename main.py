from src.dev import Dev
from src.dev_list import DevList
from src.task import Task
from src.project import Project
from src.task_list import TaskList

def main():
    """Создание объектов"""
    dev1 = Dev('devSanya@mail.ru', '111111', 'Oleg', 'Fomin', 22)
    dev2 = Dev('devNastya@mail.ru', '111111', 'Oleg', 'Fomin', 22)
    dev3 = Dev('devDaha@mail.ru', '111111', 'Oleg', 'Fomin', 22)
    dev4 = Dev('devYulia@mail.ru', '111111', 'Oleg', 'Fomin', 22)
    devlist = DevList()
    devlist.add_dev(dev1)
    devlist.add_dev(dev2)
    devlist.add_dev(dev3)
    devlist.add_dev(dev4)
    task1 = Task('create_database', 5, "t")
    task2 = Task('second_task', 3)
    task3 = Task('third_task', 3)
    task4 = Task('fourth', 3)
    # print(task1.uid)
    project_mazad = Project('Mazad')
    project_bosh = Project('Bosh')
    task_list = TaskList([task2, task3, task4])
    # print(task_list)
    dev1.add_task([task1, task2, task4, task3])
    # print(dev1)
    # print(task1.uid,task2.uid)
    """Вопрос пор добавления таск по юиду"""
    # n = {}
    # # m = dev1.task_to_do.tasks.get('517166fe85')
    # # n[1] = m
    # print(type(m))
    # print(n)
    my_list = DevList()
    my_list.add_dev([dev1, dev3])

    print(my_list) #Узнать у Саши в чем проблема, а-то уже спит наверное)


if __name__ == '__main__':
    main()

#  print(str(task1))
# print("\n", task1, "\n", task2, "\n", task3, "\n", dev1)
#   dev1.add_task(task1)
