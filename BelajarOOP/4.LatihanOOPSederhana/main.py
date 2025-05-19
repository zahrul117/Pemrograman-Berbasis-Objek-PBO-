class Hero:
    def __init__(self,name, health, attackPower, armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self, self.attackPower)
    def diserang(self, lawan, attackPowerLawan):
        print(f"{self.name} diserang {lawan.name}")
        attackDiterima = attackPowerLawan / self.armorNumber
        print(f"serangan diterima : " + str(attackDiterima))
        self.health -= attackDiterima
        print('darah ' + self.name + ' tersisa ' + str(self.health))


udin = Hero("Udin",100,20,10)
zahrul= Hero('Zahrul',150, 30, 20)

udin.serang(zahrul)
zahrul.serang(udin)