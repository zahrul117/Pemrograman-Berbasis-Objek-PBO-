class Pelajar:
    def __init__(self, nama, usia = 14, classroom="9-B"):
        self.nama = nama
        self.usia = usia
        self.classroom = classroom
    def show(self):
        print(f"Nama: {self.nama} umur {self.usia} tahun, kelas {self.classroom}")

udin = Pelajar("Udin")
udin.show()
ucup = Pelajar("ucup", 10, "9-A")
ucup.show()