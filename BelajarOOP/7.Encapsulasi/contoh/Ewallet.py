class Ewallet:
    def __init__(self, namaPemilik, saldoAwal):
        self.__nama = namaPemilik
        self.__saldo = saldoAwal

    #getter
    def getSaldo(self):
        return self.__saldo
    
    def getNama(self):
        return self.__nama
    
    #setter
    def topUp(self, jumlah):
        if jumlah > 0 :
            self.__saldo += jumlah
            print(f"{jumlah} berhasil di tambahkan ke saldo")
        else:
            print("Jumlah top up tidak valid")

    def transfer(self, jumlah):
        if jumlah > 0 and jumlah <= self.__saldo:
            self.__saldo -= jumlah
            print(f"{jumlah} berhasil ditransfer.")
        else:
            print("Transfer gagal. Saldo tidak cukup atau jumlah tidak valid.")

akunSaya = Ewallet ('udin', 500000)

print(f"Nama : {akunSaya.getNama()}")
print(f"Saldo : {akunSaya.getSaldo()}")

akunSaya.topUp(250000)
print(f"saldo sekarang {akunSaya.getSaldo()}")

akunSaya.transfer(300000)
print(f"saldo sekarang {akunSaya.getSaldo()}")

akunSaya.transfer(600000)