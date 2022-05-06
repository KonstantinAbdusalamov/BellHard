def calculator(first_number, operation, second_number):
    if operation == '*':
        result = first_number * second_number
        print(result)
    elif operation == '+':
        result = first_number + second_number
        print(result)
    elif operation == '-':
        result = first_number - second_number
        print(result)
    elif operation == '/':
        try:
            result = first_number / second_number
        except ZeroDivisionError:
            print('Ошибка. Деление на нуль')
        else:
            print(result)

first_number = int(input('Введите первое число: '))
operation = input('Введите операцию: ')
second_number= int(input('Введите второе число: '))
count = 1
while operation != 'stop':
    calculator(first_number, operation, second_number)
    operation = input('Введите знак операции')
    if operation != 'stop':
        first_number = int(input('Введите первое число: '))
        second_number = int(input('Введите второе число: '))
    count =+ 1
    print(f'Было выполнено - {count}')


