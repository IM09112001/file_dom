"""login database"""

import os
import sys
from datetime import datetime
login = input("Enter your login: ")
password = input("Enter your password: ")

with open('users.txt', 'r') as rf:
    for users in rf:
        [login_db, password_db] = users.split(' ')
        if login == login_db.rstrip() and password == password_db.rstrip():
            print(f'hi, {login}')
            with open('log.txt', 'a', encoding="utf-8") as rw:
                rw.write(f'пользователь {login} вошел в систему успешно в {datetime.now()}\n')


                break

        else:
                print(f'пользователь {login} не вошел в систему в {datetime.now()}\n')


                break





"""Login database"""
