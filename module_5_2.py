class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __len__(self):
        # Возвращаем количество этажей здания
        return self.floors

    def __str__(self):
        # Возвращаеем строку с названием и количеством этажей
        return f"Название: {self.name}, кол-во этажей: {self.floors}"


home1 = House("ЖК Эльбрус", 10)
home2 = House("ЖК Альбатрос", 16)

print(home1)
print(home2)

print(len(home1))
print(len(home2))
