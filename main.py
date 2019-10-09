from time import sleep

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
    task4.get_time()
    project_mazad = Project('Mazad')
    project_bosh = Project('Bosh')
    task_list = TaskList([task2, task3, task4])
    dev1.add_task([task1, task2, task4])

    """trecker test"""
    dev1.set_to_do(task1)
    # sleep(3)
    # print(task1.trek_time)
    # dev1.set_in_progress(task1)
    # print(task1.updated_at)
    # print(task1.trek_time)
    # sleep(4)
    # dev1.set_to_do(task1)
    # print(task1.updated_at)
    # print('tut')
    # print(task1.trek_time)
    # sleep(3)
    # print(task1.trek_time)
    # print(task1.updated_at)
    # dev1.set_in_progress(task1)
    # sleep(5)
    # dev1.set_resolve(task1)
    # print('tut')
    # print(task1.trek_time)
    dev1.show_all_dev_task()
    print(dev1.show_to_do_task())
    task1.change_status_on_resolve()
    print(task1.status)


if __name__ == '__main__':
    main()
