class Mahasiswa:
    def __init__(self,nama,umur):
        self.__nama = nama #private variable
        self.__umur = umur #private variable

    def info(self):
        print(f"Nama : {self.__nama}, Umur : {self.__umur}")

mhs = Mahasiswa("Udin", 99)
mhs.info()

print(mhs.__nama)
# print(mhs._Mahasiswa__nama)