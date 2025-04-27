class Buku:
    def __init__(self, judul, pengarang, tahun):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun = tahun


judul = input("Masukkan Judul Buku : ")
pengarang = input("Masukkan Nama Pengarang : ")
tahun = input('masukkan Tahun terbit : ')

buku1 = Buku(judul, pengarang, tahun)

print(f"Judul : {buku1.judul}")
print(f"pengarang : {buku1.pengarang}")
print(f"tahun : {buku1.tahun}")