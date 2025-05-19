class xParameter:
    def __init__(self, nama, umur, salary):
        self.nama = nama
        self.umur = umur
        self.salary = salary
    def show(self):
        print(f"{self.nama} {self.umur} {self.salary}")

rul = xParameter("Rul", 20, 1000000)
rul.show()
udin = xParameter("udin",5,10000000)
udin.show()