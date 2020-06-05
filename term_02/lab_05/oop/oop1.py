from random import randint

class Warrior:
    def __init__(self, name):
        self.health = 100
        self.name = name
    
    def hit(self, other_warrior):
        self.health -= 20
        print( '{} got hit by {}. His health is {}.'.format(self.name, other_warrior.name, self.health) )
        if self.health == 0:
            print('{} is dead!'.format(self.name))


warriors = [Warrior('Arthur'), Warrior('Luther')]

while warriors[0].health != 0 and warriors[1].health != 0:
    i = randint(0, 1)
    warriors[i].hit(warriors[(i + 1) % 2])
