class Hewan:
    def __init__(self, name, jenis, umur):
        self.name = name
        self.jenis = jenis
        self.umur = umur


hewan1 = Hewan('Kitty',"kucing", 2)

print(f"Nama : {hewan1.name}")
print(f"Jenis : {hewan1.jenis}")
print(f"Umur : {hewan1.umur} tahun")