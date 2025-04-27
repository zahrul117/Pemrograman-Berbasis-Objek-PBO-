class Hero:
    #class variabel
    jumlah = 0
    def __init__(self,inputName, inputHealth, inputPower, inputArmor):
        #instance Variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print('membuat Hero dengan nama ' + inputName)

hero1 = Hero('Udin',3000, 6000, 2000)
print(Hero.jumlah)
hero2 = Hero('Budi',4000, 3000, 1000)
print(Hero.jumlah)
