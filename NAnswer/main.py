"""2 задание: Пользователь должен ввести 10 чисел, которые нужно записать в столбик в файле numbers.txt.
 После нужно считать этот же файл, найти сумму и всех этих чисел и записать ответ в файл answer.txt
"""

import os
import sys
inOut = open('number.txt', 'w')
n = int(input("Items number: "))
a = []
print("Write items: ")
for i in range(n):
    i = input()
    a.append(i+'\n')
# print(a)
inOut.writelines(a)
inOut.close()
inIn = open('number.txt', 'r').read()
answer = open('answer.txt', 'w')
readNums = inIn.split("\n")
print(readNums)
summ = sum(list(map(int, readNums[:len(readNums)-1])))
a.append(str(summ))
answer.write("".join(a))
"""2-задание"""

