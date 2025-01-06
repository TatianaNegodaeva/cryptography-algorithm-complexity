import random #добавление ф-ии рандом

list = [] #пустой список
n = int(input()) #кол-во чисел в списке
a = 0

for i in range(n): #заполнение списка случайными числами
    number = random.randint(1, 101)
    list.append(number)

print(list) #вывод полученного списка

for i in range(n-1): #прогонки (n-1 раз)
    for j in range(n-1-i): #номер числа в списке
        if list[j] > list[j+1]:
            a = list[j]
            list[j] = list[j+1]
            list[j+1] = a

print(list)