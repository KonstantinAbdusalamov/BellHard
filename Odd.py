list1 = [int (i) for i in input('Введите список чисел').split()]
def even(num):
    return num % 2==0

for i in list1:
    if i == 139:
        print('Найдено число 139.Останавливаю цикл')
        break
    if not even(i):
        print(i)


