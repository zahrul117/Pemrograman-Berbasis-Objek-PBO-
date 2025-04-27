class Hero:
    def __init__(self,inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = Hero('Udin',3000, 6000, 2000)

print(hero1.name)