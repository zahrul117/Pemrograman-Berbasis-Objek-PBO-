class Kendaraan:
    jumlahKendaraan = 0

    def __init__(self, tipe, merk):
        self.tipe = tipe
        self.merk = merk
        Kendaraan.jumlahKendaraan += 1
    
    def tampilkanJumlahKendaraan():
        print(f"Jumlah kendaraan di garasi : {Kendaraan.jumlahKendaraan}")


kendaraan1 = Kendaraan('Mobil', "Toyoya")
kendaraan2 = Kendaraan('motor','honda')
kendaraan3 = Kendaraan('Mpbil',"Bmw")

Kendaraan.tampilkanJumlahKendaraan()