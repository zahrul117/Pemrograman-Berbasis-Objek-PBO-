class Siswa:
    sekolah = 'SMP Negeri 00 Jambi'
    sekolah2 = 'SD Negeri 00 Jambi'

    def __init__(self, nama, usia, alamat):
        self.nama = nama
        self.usia = usia
        self.alamat = alamat
    
s1 = Siswa("udin", 10, "Mayang - jambi")
print("="*20, "DATA SEKOLAH", "="*20)
print(f"nama siswa : {s1.nama} Umur Anak : {s1.usia} dan alamat {s1.alamat}")
# access class variable
print('nama sekolah :', Siswa.sekolah2)
print ("=" * 25, "Data Sekolah ", "=" * 25)

# modify instance variables
s1.nama = 'andika surya putra'
s1.usia = 14
s1.alamat="talang banjar - jambi"
print('nama siswa :', s1.nama, " dan umur anak : ", s1.usia)
# access class variale
print('nama sekolah :', Siswa.sekolah)