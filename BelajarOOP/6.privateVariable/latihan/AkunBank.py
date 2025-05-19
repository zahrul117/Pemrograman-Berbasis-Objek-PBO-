class AkunBank:
    def __init__(self, nama, saldo):
        self.__namaPemilik = nama
        self.__saldo = saldo

    def lihatSaldo(self):
        print(f"nama : {self.__namaPemilik} dan saldo anda : {self.__saldo}")

    def setor(self, uang):
        self.__saldo += uang

    def tarik(self, uang):
        self.__saldo -= uang

akun1 = AkunBank("Budi", 0)
akun1.setor(600000)
akun1.tarik(250000)
akun1.lihatSaldo()

# print(akun1.__nama__pemilik) #harus error