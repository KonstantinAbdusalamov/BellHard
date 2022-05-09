'''n = int(input('Введите номер месяца'))
def month_to_season(n):
    if  n == 1 or n == 2 or n == 12:
        return 'Зима'
    elif n == 3 or n == 4 or n == 5:
        return 'Весна'
    elif  n == 6 or n == 7 or n == 8:
        return 'Лето'
    elif  n == 9 or n == 10 or n == 11:
        return 'Осень'
print(month_to_season(n))'''

n = int(input('Введите номер месяца'))
def month_to_season(month):
    seasons = {(1,2,12): 'Зима',
               (3,4,5): 'Весна',
               (6, 7, 9): 'Лето',
               (9,10,11): 'Осень'}
    season = None
    for key, value in seasons.items():
        if month in key:
            season = value
            break

    return season
print(month_to_season(n))
