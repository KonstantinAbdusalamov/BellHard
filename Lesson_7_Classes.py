class Counter:

    def __init__(self, some_value=0, some_increase=1,some_decrease=1):
        self.value = some_value
        self.increase = some_increase
        self.decrease = some_decrease

    def __iter__(self):
        return self.value + self.increase

    def __next__(self):
        return self.value - self.decrease


a1 = Counter(5)
print(a1.__iter__())
b1 = Counter()
print(b1.__iter__())
a2 = Counter(15)
print(a2.__next__())
b2 = Counter()
print(b2.__next__())


class Phone:

    def __init__(self, some_brand, some_model, some_issue_year, some_name):
        self.brand = some_brand
        self.model = some_model
        self.issue_year = some_issue_year
        self.name = some_name

    def receive_call(self):
        return f"Звонит {self.name}"

    def get_info(self):
        a = (self.brand, self.model, self.issue_year)
        return a

    def __str__(self):
        return f"Бренд: {self.brand} Модель: {self.model} Год выпуска: {self.issue_year}"

c1 = Phone('Лада', 'С5', 1980, 'Иван')
print(c1.receive_call())
print(c1.get_info())
print(c1.__str__())