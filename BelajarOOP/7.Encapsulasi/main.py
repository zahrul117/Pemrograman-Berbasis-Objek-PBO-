class Hero: 
    def __init__(self, name, health, attackPower):
        self.__name = name
        self.__health = health
        self.__attPower = attackPower

    #getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health

    #setter
    def diSerang(self, serangPower):
        self.__health -= serangPower

    def setAttPower(self, nilaiBaru):
        self.__attPower = nilaiBaru

#awal dari game
udin = Hero("Udin", 100, 10)

print(udin.getName())
print(udin.getHealth())
udin.diSerang(30)
print(udin.getHealth())
udin.setAttPower(15)
udin.diSerang(15)
print(udin.getHealth())