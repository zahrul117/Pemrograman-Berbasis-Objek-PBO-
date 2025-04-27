class Belanja:
    def __init__(self, produk, harga):
        self.produk = produk
        self.harga = harga

    #method untuk menghitung diskon 
    def hitungDiskon(self, persenDiskon):
        return self.harga * (persenDiskon / 100)
    
    #method untuk menghitung harga setelah diskon
    def hargaSetelahDiskon(self, persenDiskon):
        diskon = self.hitungDiskon(persenDiskon)
        return  self.harga - diskon

#membuat objek belanja 1
belanja1 = Belanja("laptop", 15000000)

#menghitung harga setelah diskon 20%
hargaDiskon = belanja1.hargaSetelahDiskon(20)
print(f"harga setelah diskon : {hargaDiskon}")

#menghitung diskon yang diterima
diskon = belanja1.hitungDiskon(20)
print(f"diskon yang diterima : {diskon}")