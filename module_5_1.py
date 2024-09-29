class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for i in range( 1, new_floor + 1):
                print(i)

h1 = House('ЖК Вертикаль', 22)
h2 = House('ДК Скворечник', 3)
h3 = House('ЖК Матрица', 18)
h4 = House('Изба', 1)
h1.go_to(5)
h2.go_to(8)
h3.go_to(4)
h4.go_to(6)
