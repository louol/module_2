class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h3 = House('ЖК Эверест', 15)
h4 = House('ЖК Тополь', 30)

# __str__
print(h1)
print(h2)
print(h3)
print(h4)

# __len__
print(len(h1))
print(len(h2))
print(len(h3))
print(len(h4))