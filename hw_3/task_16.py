# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

size = int(input('Input count of elements in list:\n'))
list = []
i = 0
while i < size:
    list.append(int(input('input number...')))
    i += 1
print(list)
magicNumber = int(input('what number do we search?'))
count = 0
for j in list:
    if j == magicNumber:
        count += 1
if count > 0:
    print(count)
else:
    print('there is no number you searched for')