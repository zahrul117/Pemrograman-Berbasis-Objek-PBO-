class Pahlawanku:
    def __init__(self, nama, hero, about):
        self.nama = input("Nama Pahlawan : ")
        self.hero = hero
        self.about = about

    def showInfo(self):
        print(f"{self.nama} sebagai pahlawan {self.hero} dan {self.about}")

class Revolusi(Pahlawanku):
    def __init__(self,name = ()):
        print("="*35, "Pahlawanku","=" * 35)
        super().__init__(name, "Revolusi", "Gugur Karena kebiadaban PKI.")
        super().showInfo()

class Nasional(Pahlawanku):
    def __init__(self, name=()):
        super().__init__(name,"Nasional ","Panglima Perang Kemerdakaan")
        super().showInfo()

class Guru(Pahlawanku):
    def __init__(self, name=()):
        super().__init__(name,"Pahlawan Tanpa Tanda Jasa","Jasa Jasamu Sangat Berharga")
        super().showInfo()

Rev = Revolusi()
Nas = Nasional()
NN = Guru()
PAH = Pahlawanku('pahlawan', 'pahlawan', 'pahlawan')
PAH.showInfo()
print("Hore Saya Berhasil Boss")
print("="*32, "SELESAI", "=" *32)