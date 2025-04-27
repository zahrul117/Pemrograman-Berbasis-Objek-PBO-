class Pesanan:
    total_pesanan = 0
    
    def __init__(self, nama_pembeli, item_pesanan):
        self.nama_pembeli = nama_pembeli
        self.item_pesanan = item_pesanan
        Pesanan.total_pesanan += 1

    def tampilkanTotalPesanan():
        print(f"Total Pesanan yang diterima : {Pesanan.total_pesanan}")

pesanan1 = Pesanan('Udin', "laptop")
pesanan2 = Pesanan('Budi', 'HP')
pesanan3 = Pesanan('nana', 'Komputer')

Pesanan.tampilkanTotalPesanan()
