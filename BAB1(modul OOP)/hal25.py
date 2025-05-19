#super class dan objek menggunakan string input
class Pahlawanku:
    def __init__(self, name, hero, about):
        self.name = input("Nama Pahlawan : ")
        self.hero = hero
        self.about = about
    def showInfo(self):
        print(f'{self.name} sebagai pahlawan {self.hero} dan {self.about}')

#sub class Revolusi
class Revolusi(Pahlawanku):
    def __init__(self,name=()):
        print("="*25, "Pahlawanku","="*25)
        #menggunakan SuperClass untuk pahlawanku dan constructor
        super().__init__(name,"Revolusi","Gugur Karena Kebiadaban PKI.")
        super().showInfo()

#sub class Nasional
class Nasional(Pahlawanku):
    def __init__(self, name=()):
        super().__init__(name,"Nasional","Panglima perang kemerdekaan")
        super().showInfo()

#sub Class Guru
class Guru(Pahlawanku):
    def __init__(self, name=()):
        super().__init__(name,"Pahlawan Tanpa Tanda Jasa","Jasa Jasamu Sangat Berharga")
        super().showInfo()

#menciptakan New Objek rev, nas,dan nn
Rev = Revolusi()
Nas = Nasional()
Guru = Guru()
print("Hore Saya berhasil Boss")
print("="*25, "Pahlawanku","="*25)