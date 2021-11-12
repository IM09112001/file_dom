"""1-задание
У вас есть файл shop.txt
Нужно считать информацию с него и вывести шаблонные предложения для каждого продукта.

Пример: There are 10 fridges, price is 900$ per item"""


import os
import sys
shopReader = open('shop.txt', 'r').read()
slited_shop = shopReader.split('\n')

for elem in range(0, len(slited_shop), 2):
    name, (countity, cost) = slited_shop[elem], slited_shop[elem+1].split()

    print(f'There are {countity} {name}, price is {cost}$ per item')
#shopReader.close()

"""1-задание"""
