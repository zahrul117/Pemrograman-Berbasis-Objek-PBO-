class Mobil:
    jumlah_mobil = 0
    def __init__(self, merek, model, tahun):
        self.merek = merek
        self.model = model
        self.tahun = tahun
        Mobil.jumlah_mobil += 1
    
    def infoMobil(self):
        print(f"merek mobil {self.merek}, model mobil {self.model}, tahunnya : {self.tahun}")

    def ubahTahun(self, tahunBaru):
        self.tahun = tahunBaru

    @staticmethod
    def infoGaransi():
        print('Garansi mobil berlaku selama 5 tahun sejak tahun pembelian')

mobil1 = Mobil('toyota','camry',2020)
mobil2 = Mobil('honda','civic',2019)

mobil1.infoMobil()
mobil2.infoMobil()

mobil1.ubahTahun(2025)
mobil1.infoMobil()
mobil1.infoGaransi()