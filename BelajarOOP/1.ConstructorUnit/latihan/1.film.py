class Film:
    def __init__(self, judul, sutradara, tahun_rilis):
        self.judul = judul
        self.sutradara = sutradara
        self.tahun_rilis = tahun_rilis


film1 = Film('Interstellar',"Christoher Nolan", 2014)

print(f"Judul Film : {film1.judul}")
print(f"Sutradara : {film1.sutradara}")
print(f"tahun rilis : {film1.tahun_rilis}")