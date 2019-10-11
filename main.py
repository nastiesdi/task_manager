from time import sleep

from src.dev import Dev
from src.dev_list import DevList
from src.task import Task
from src.project import Project
from src.task_list import TaskList


def main():
    """Создание объектов"""
    dev1 = Dev('devSanya@mail.ru', password='123456', first_name='Alexander', last_name='Gubin', age=21)
    dev2 = Dev('devNastya@mail.ru', password='123412312', first_name='Nastya', last_name='Davydzenka', age=21)
    dev3 = Dev('devDaha@mail.ru', password='123456', first_name='Daria', last_name='Shkuratova', age=21)
    dev4 = Dev('devYulia@mail.ru', password='123456ss', first_name='Yulia', last_name='Filon', age=20)
    dev5 = Dev('devLena@mail.ru', password='123456rrr', first_name='Alex', last_name='Kazackevich', age=26)
    task1 = Task('create_database', 5, "t")
    task2 = Task('add_field_task2', 3)
    task3 = Task('add_field_task3', 4)
    task4 = Task('fourth', 3)
    task5 = Task('five', 3)
    task6 = Task('Six', 1)
    task7 = Task('Seven', 2)
    task8 = Task('eignt', 3)
    task9 = Task('nine', 1)
    task10 = Task('ten', 2)
    project_mazad = Project('Mazad')
    project_bosh = Project('Bosh')
    task_list = TaskList([task2, task3, task4])
    devlist = DevList()
    devlist.add_dev([dev1, dev2, dev3, dev4, dev5])
    task1.add_sub_tasks(task2)
    task2.add_sub_tasks(task3)
    task2.add_sub_tasks(task4)
    task4.add_sub_tasks(task5)
    print(str(devlist) + '\n')
    print('One of our developer\n' + str(dev1)+ '\n')
    print('Changing email and password:\n 1.Use incorect old password')
    dev1.change_email('newemaildevSanya@gmail.com')
    dev1.change_password('newpassword123', 'newpassword123')
    print('email: ' + dev1.email)
    print('password: ' + dev1.password)
    print(' 2. Use correct old password')
    dev1.change_password('123456', 'newpassword123')
    print('new password is: ' + str(dev1.password))
    print('\n Add task to dev')
    dev1.add_task([task1, task2, task6, task7, task8, task9, task10])
    print(dev1)
    print('\n Remove devs task: "add_field_task2"')
    dev1.remove_task_absolut(task2)
    print(dev1)
    print('\nShow all dev tasks')
    print(dev1.show_all_dev_task())
    print('\nShow all to do tasks')
    print(dev1.task_to_do)
    print('\nChange tasks status on in process\n To do tasks:')
    dev1.set_in_progress(task7)
    print(dev1.task_to_do)
    print('Tasks in progress:')
    print(dev1.task_in_progress)
    sleep(1)
    print('\nchange status task on to do ( time_track is chenged)')
    dev1.set_to_do(task7)
    print(dev1.task_to_do)
    print('Tasks in progress:')
    print(task7.trek_time)





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
