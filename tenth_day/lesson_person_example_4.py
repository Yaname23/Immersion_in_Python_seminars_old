class Person:
    max_up = 3

    def __init__(self, name, race='unknown'):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100

p1 = Person('Silva', 'elf')
p2 = Person('Ivan', 'human')
p3= Person('Grog')

print(f'{p1.name = },{p1.race= }')
print(f'{p2.name = },{p2.race= }')
print(f'{p3.name = },{p3.race= }')