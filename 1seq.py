el_qnty = int(input('Введите количество элементов: '))
lst = []
for i in range(el_qnty):
    lst.append(input('Введите '+ str(i + 1) + ' элемент: '))
lst.sort()
print('Вывод:', lst)
