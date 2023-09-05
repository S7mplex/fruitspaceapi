import FruitSpaceAPI
gdps = FruitSpaceAPI.GDPS('01KG')

print(gdps.getComments(31, 0)) # Первый аргумент - ID уровня, второй - страница
