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
    dev5 = Dev('devLena@mail.ru', '111111', 'Oleg', 'Fomin', 22)
    dev6 = Dev('devIra@mail.ru', '111111', 'Oleg', 'Fomin', 22)
    # dev1.show_all_dev_task()
    # print(dev1)
    devlist = DevList()
    devlist.add_dev(dev1)
    devlist.add_dev(dev2)
    devlist.add_dev(dev3)
    devlist.add_dev(dev4)
    task1 = Task('create_database', 5, "t")
    task2 = Task('second_task', 3)
    task3 = Task('third_task', 3)
    task4 = Task('fourth', 3)
    task5 = Task('five', 3)
    task4.get_time()
    project_mazad = Project('Mazad')
    project_bosh = Project('Bosh')
    task_list = TaskList([task2, task3, task4])
    dev1.add_task(task1)

    task1.add_sub_tasks(task2)
    task2.add_sub_tasks(task3)
    task2.add_sub_tasks(task4)
    task4.add_sub_tasks(task5)
    # print('Sub_task:')
    task1.show_all_sub_tasks()
    task2.remove_one_subtask(task3)
    print('new2')
    task1.show_all_sub_tasks()
    print('new3')
    print(task3.show_sub_tasks())

    # print('new' + str(task1.show_all_sub_tasks()))

    # print(task1.sub_tasks())

    # print(task2.show_sub_tasks())

    """trecker test"""
    # dev1.set_to_do(task1)
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
    # dev1.show_all_dev_task()
    # print(dev1.show_to_do_task())
    # task1.change_status_on_resolve()
    # print(task1.status)




if __name__ == '__main__':
    main()
