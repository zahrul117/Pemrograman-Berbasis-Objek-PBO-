class Hero:
    #class variabel
    jumlahHero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlahHero += 1
    
    #void function, method tanpa return
    def siapa(self):
        print(f"Nama Hero = {self.name}")

    #method dengan argumen
    def tambahDarah(self, up):
        self.health += up

    #method dengan return
    def getHealth(self):
        return self.health


hero1 = Hero('Udin', 1000,100,10)
hero2 = Hero('budi',2000,300,10)

hero2.siapa()
hero1.tambahDarah(50)

print(hero1.getHealth())