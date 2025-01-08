import random #добавление ф-ии рандом

list = [] #пустой список
n = int(input()) #кол-во чисел в списке

for i in range(n): #заполнение списка случайными числами
    number = random.randint(1, 100)
    list.append(number)
    
print(list) #вывод полученного списка

correct_list = list

for i in range(0, n): #прогонка по всем элементам списка
    left = [] #список чисел меньше сравниваемого
    right = [] #список чисел больше сравниваемого
    middle = [] #список чисел равных сравниваемому
    elem = list[i] #элемент для сравнения из изначального списка
    for j in range(0, n): #прогонка по элементам отсортированного списка
        run_elem = correct_list[j] #элемент отсортированного списка для сравнения
        if elem > run_elem: #сравнение элементов из двух списков
            left.append(run_elem)
        elif elem == run_elem:
            middle.append(run_elem)
        elif elem < run_elem:
            right.append(run_elem)
    correct_list = left + middle + right #обновление отсортированного списка после сравнения элементов
            
print(correct_list) #вывод отсортированного списка