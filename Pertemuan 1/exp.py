class Person:
    def __init__(self, nama, sex, profession):
        self.nama = nama
        self.sex = sex
        self.profession = profession
    def show(self):
        print(f"nama : {self.nama} Sex = {self.sex} Profession = {self.profession}")
    def work(self):
        print(f"{self.nama}, working as a, {self.profession}")


nama = input("Masukkan Nama : ")
sex = input("Masukkan Jenis Kelamin : ")
profession = input("Masukkan Pekerjaan : ")

nama2 = Person(nama, sex, profession)
zahrul = Person("Zahrul","Male","Software Engineer")
nama2.show()
zahrul.show()
zahrul.work()