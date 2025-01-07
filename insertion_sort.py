import random #добавление ф-ии рандом

list = [] #пустой список
n = 5 #кол-во чисел в списке
a = 0

for i in range(n): #заполнение списка случайными числами
    number = random.randint(1, 101)
    list.append(number)
    
print(list) #вывод полученного списка

for i in range(0, n-1): #прогонка по всем значениям списка
    if list[i] > list[i+1]: 
        a = list[i+1] #сохранение меньшего из сравниваемых
        for j in range(i, -1, -1): #прогонка по предыдущим значениям в списке
            if a < list[j]: 
                list[j+1] = list[j] 
                list[j] = a 
            
print(list) #вывод отсортированного списка