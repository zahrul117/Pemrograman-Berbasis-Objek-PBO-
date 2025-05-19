class Pelajar:
    def __init__(self, nama=(), usia=(), classroom=()):
        self.nama = input("Nama Siswa : ")
        self.usia = input("Umur Siswa : ")
        self.classroom = input("Kelas Siswa : ")

    def show(self):
        print(f"Nama Siswa : {self.nama} Umur Siswa : {self.usia} Kelas Siswa : {self.classroom}")

zahrul = Pelajar()
zahrul.show()
print("="*50)
udin = Pelajar('udin',10,5)
udin.show()