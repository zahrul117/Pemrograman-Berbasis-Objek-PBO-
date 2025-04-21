class Kotak:
    def __init__(self, nama):
        self.nama = nama

    def tampilkan(self):
        print(f"Ini adalah {self.nama}")

class Kubus(Kotak):
    def kubus_info(self):
        print("Kubus punya 6 sisi yang sama panjang.")

class Balok(Kotak):
    def balok_info(self):
        print("Balok memiliki panjang, lebar, dan tinggi yang berbeda.")

class Kerucut(Kotak):
    def kerucut_info(self):
        print("Kerucut memiliki alas lingkaran dan satu titik puncak.")

# Membuat objek
kotak1 = Kubus("Kubus")
kotak2 = Balok("Balok")
kotak3 = Kerucut("Kerucut")

# Memanggil method dari parent dan method khusus
kotak1.tampilkan()
kotak1.kubus_info()

kotak2.tampilkan()
kotak2.balok_info()

kotak3.tampilkan()
kotak3.kerucut_info()
