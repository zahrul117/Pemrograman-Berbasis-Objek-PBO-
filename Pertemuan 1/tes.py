class Mobil:
    def __init__(self, merk, tahun, tipe):
        self.merk = merk
        self.tahun = tahun
        self.tipe = tipe

    def info(self):
        print(self.merk, self.tahun, self.tipe)

mobil = Mobil("Toyota", 1999, "Basenglah")
mobil.info()