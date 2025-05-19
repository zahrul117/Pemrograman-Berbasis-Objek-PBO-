class Rumah:
    #instance attribute
    def __init__(self, bahan, harga, lokasi, model):
        # self adalh instance dari class
        self.bahan = bahan
        self.harga = harga
        self.lokasi = lokasi
        self.model = model
    def show(self):
        print(f"Bahan bangunan : {self.bahan} harga: {self.harga}")
    def gaya(self):
        print(f"Rumah idamanku {self.model} dan lokasinya {self.lokasi}")

#membuat objek
rumah1 = Rumah("Kayu",7000000,"pedesaan","Britania Clasic")
rumah2 = Rumah("Beton",15000000,'Perkotaan','classic modern')
rumah1.show()
rumah1.gaya()
print("="*60)
rumah2.show()
rumah2.gaya()

