txt = input('Введите элементы списка через один из разделителей - , ; /: ')
txt = txt.replace('/', ',')
txt = txt.replace(';', ',')
lst = txt.split(',')
lst.sort()
i = 1
while i < len(lst):
    if lst[i - 1] == lst[i]:
        lst.pop(i)
    else:
        i += 1
print('Результат:', lst)