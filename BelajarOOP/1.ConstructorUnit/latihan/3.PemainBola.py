class PemainBola:
    def __init__(self, nama, posisi, klub):
        self.nama = nama
        self.posisi = posisi
        self.klub = klub

pemain1 = PemainBola('Pedri', 'Gelandang', "Barcelona")

print(f"Nama Pemain : {pemain1.nama}")
print(f"Posisi : {pemain1.posisi}")
print(f"klub : {pemain1.klub}")