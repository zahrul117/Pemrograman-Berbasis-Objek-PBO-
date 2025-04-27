class Person:


    def hitungUmur(tahunLahir, tahunSekarang=2025):
        return tahunSekarang - tahunLahir
    
tahunLahir = 2000
umur = Person.hitungUmur(tahunLahir)
print(f"umur : {umur} tahun")