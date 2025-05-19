class Orang:
    def __init__(self, nama, jenis, profession):
        self.nama = nama
        self.jenis = jenis
        self.profession = profession

    def show(self):
        print(f"nama : {self.nama} jenis Kelamin : {self.jenis} Profesi : {self.profession}")
    
    def work(self):
        print(f"{self.nama} sedang bekerja sebagai {self.profession}")

zahrul = Orang('zahrul','laki-laki','software engineer')

zahrul.show()
zahrul.work()