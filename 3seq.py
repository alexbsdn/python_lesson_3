txt = input('Введите элементы 1-го списка через один из разделителей - , ; /: ')
txt = txt.replace('/', ',')
txt = txt.replace(';', ',')
lst1 = txt.split(',')
txt = input('Введите элементы 2-го списка через один из разделителей - , ; /: ')
txt = txt.replace('/', ',')
txt = txt.replace(';', ',')
lst2 = txt.split(',')
i = j = 0
for i in range(len(lst2)):
    for j in range(lst1.count(lst2[i])):
        lst1.remove(lst2[i])
print ('Результат:', lst1)