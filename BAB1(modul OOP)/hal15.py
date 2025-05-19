class Siswa:
    #class variabel
    sekolah = 'SMP Negeri 00 Jambi'
    sekolah2 = "SD Negeri 00 Jambi"
    #constructor
    def __init__(self, nama, usia, alamat):
        #instance variabel
        self.nama = nama
        self.usia = usia
        self.alamat = alamat

s1 = Siswa("Udin","10","Mayang-Jambi")
print("="*20, "Data Sekolah", "="*20)
#access instance variabel
print(f'Nama siswa : {s1.nama} Umur anak : {s1.usia} dan Alamat : {s1.alamat} ')

#access class variable
print(f'Nama Sekolah : {Siswa.sekolah2}')
print("="*20, "Data Sekolah", "="*20)

#modify instance variabel
s1.nama = "Udin2"
s1.usia = 11
s1.alamat = "Jambi"
print(f'Nama Siswa {s1.nama} dan umur anak : {s1.usia}')

#access class variable
print(f'Nama Sekolah : {Siswa.sekolah}')