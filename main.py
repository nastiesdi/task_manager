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
    project_mazad = Project('Mazad')
    project_bosh = Project('Bosh')
    task_list = TaskList([task2, task3, task4])
    print(task_list)
    dev1.add_task([task1, task2, task4, task3])
    print(dev1)
    print(task1.uid,task2.uid)
    dev1.show_to_do_task()
    # print(task_list.get_all_task())
    # #          Task('five_task', 3)]
    # # task5 = [Task('seven', 3),
    # #          Task('eight', 3)]
    # # print(task1)
    # # print(task1.priority_task)
    # # task1.change_status_taskask('Completed')
    # # print(str(task2))




    # """использование методов"""
    # task1.change_status_task('Close')
    # task1.change_priority_task(2)
    # dev1.add_task(task2)
    # dev1.add_task(task3)
    # dev1.add_task(task5)
    # print(dev1)# если мы прописываем переменную задачи при создании, то выводится обработанная информация,
    # # если добавляем - то ссылка на объект
    # #print(task1)
    # print(dev1.show_all_dev_task())
    # task2.add_executor_for_task(dev1)
    # print(task2)
    # dev1.add_task(task4)
    # project_bosh.add_task_to_project(task4)
    # print(project_bosh.task)
    # project_bosh.add_task_to_project(task1)
    # print(dev1.task)
    # print(project_bosh.task) #выводятся ссылки на объекты, а хочу чтобы обрабатывались
    #
    # #<test> add tast to project
    #
    # project_bosh.add_task_to_project(task4)
    # print(project_bosh.task)
    # project_bosh.add_task_to_project(task1)
    # print(project_bosh)
    #
    # print(Task)
if __name__ == '__main__':
    main()

#  print(str(task1))
# print("\n", task1, "\n", task2, "\n", task3, "\n", dev1)
#   dev1.add_task(task1)
