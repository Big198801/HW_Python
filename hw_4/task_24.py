# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора
# на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
n = int(input("сколько у нас кустов? : "))
new_array = list()
for i in range(n):
    new_array.append(int(input('введите число ягод: ')))
max_yagod = 0
for i in range(n):
    if max_yagod < (sum := new_array[i-2] + new_array[i-1] + new_array[i]):
        max_yagod = sum
print(new_array, sum)