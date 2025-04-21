class Rumah:
    def __init__(self, bahan, harga, lokasi, model):
        self.bahan = bahan
        self.harga= harga
        self.lokasi = lokasi
        self.model = model
    
    def show(self):
        print(f"bahan bangunan : {self.bahan} harga : {self.harga}")
    def gaya(self):
        print(f"Rumah idamanku : {self.model} dan lokasinya : {self.lokasi}")


#membuat objek
rumah1 = Rumah('Kayu', 700000000, 'pendesaan', 'Britania clasic')
rumah2 = Rumah('Beton',150000000, "perkotaan", "Clasic modern")

rumah1.show()
rumah1.gaya()
print("=" * 60)
rumah2.show()
rumah2.gaya()