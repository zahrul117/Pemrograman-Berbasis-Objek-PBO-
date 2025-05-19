class Mamalia(object):
    def __init__(self, namaHewan):
        self.namaHewan = namaHewan
        print(f"{self.namaHewan} adalah hewan berdarah panas")

class Harimau(Mamalia):
    def __init__(self):
        print('Harimau adalah hewan kaki 4')
        super().__init__('harimau')
m1=Harimau()
class Sea():
    def __init__(self, laut):
        print(f"{laut} adalah hewan berdarah dingin")

class Lumba2(Sea):
    def __init__(self):
        print('lumba-lumba adalah hewan mamalia yang hidup di laut')
        super().__init__('Lumba-Lumba')
m2 = Lumba2