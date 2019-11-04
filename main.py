import argparse
import pickle

from src.dev import Dev
from src.task import Task
from src.project import Project
from manager import Manager
from helpers.consts import STATUS_LIST, PROJ_LIST, PRIORITY, DEV_LIST, TASK_LIST


def parse_args():
    '''
        Добавить везде нормальный хелр, чтобы было похоже на прод вариант
    :return:
    '''
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    reg_parser = subparsers.add_parser('reg_user')
    reg_parser.add_argument('-e', '--email', type=str, help='The email must match the mask aa@ja.ar')
    reg_parser.add_argument('-p', '--password', type=str, help='Password must contain from 5 to 25 characters, at least'
                                                               ' 1 character of upper case, lower case and number ')
    reg_parser.add_argument('-r', '--repeat_password', type=str, help='Password and repeat password must match')
    reg_parser.add_argument('-f', '--first_name', type=str, help='First name must be between 2 and 15 latin characters')
    reg_parser.add_argument('-l', '--last_name', type=str, help='Last name must be between 2 and 15 latin characters')
    reg_parser.add_argument('-a', '--age', type=int, help='Age must be between 16 and 100')
    reg_parser.set_defaults(func=manager.registration)

    login_parser = subparsers.add_parser('login')
    login_parser.add_argument('-e', '--email', help='The entered email must be contained in the database')
    login_parser.add_argument('-p', '--password', help='Password must be valid for the entered email')
    login_parser.set_defaults(func=manager.login)
    # email, old_password, new_password, repeat_new_password)

    change_password_pars = subparsers.add_parser('change_password')
    # change_password_pars.add_argument('-e', '--email')
    change_password_pars.add_argument('-o', '--old_password')
    change_password_pars.add_argument('-n', '--new_password')
    change_password_pars.add_argument('-r', '--repeat_new_password')
    change_password_pars.set_defaults(func=manager.change_password)


    args = parser.parse_args()
    if 'func' in args:
        args.func(args)
        # print(args)


def main():

    # parse_args()
    dev1 = Dev(email='dev@hn', password='123456Qq', repeat_password='123456Qq', first_name='Alexander',
               last_name='Gubin', age=21)
    dev1.add_to_dev_list()
    manager.developers[dev1.email] = dev1
    parse_args()
    task1 = Task('create_database', 'Medium')



if __name__ == '__main__':
    manager = Manager()
    # with open('login.pkl', 'rb') as infile:
    #     manager = pickle.load(infile)
    main()
