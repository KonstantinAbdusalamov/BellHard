
text_first = input('Введите первое число: ')
number_first = int(text_first)
operation = input('Введите операцию: ')
text_second = input('Введите второе число: ')
number_second = int(text_second)
if operation == '*':
    result = number_first * number_second
    print(result)
elif operation == '+':
    result = number_first + number_second
    print(result)
elif operation == '-':
    result = number_first - number_second
    print(result)
elif operation == '/':
    if number_second == 0:
        print('Ошибка. Деление на нуль')
    else:
        result = number_first / number_second
        print(result)

# print("Ответ:", test_number)
