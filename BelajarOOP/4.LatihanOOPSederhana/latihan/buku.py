class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahunTerbit = tahun_terbit

    def info(self):
        print(f"judul buku : {self.judul} pengarang : {self.pengarang} dan tahun terbit {self.tahunTerbit}")

    def ubahTahun(self,tahun_baru):
        self.tahunTerbit = tahun_baru
        print(f"tahun terbit di ubah menjadi : {self.tahunTerbit}")

buku1 = Buku('laut bercerita','leila s chudori', 2019) 
buku1.info()
buku1.ubahTahun(2020)
buku1.info()