class AkunBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo

    #method untuk menambahkan saldo
    def deposit(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            print(f"deposito berhasil. Saldo saat ini: {self.saldo}")
        else:
            print('Jumlah deposito harus lebih dari 0')

    #method untuk menarik saldo
    def tarik(self, jumlah):
        if jumlah <= self.saldo and jumlah > 0:
            self.saldo -= jumlah
            print(f"anda menarik sebesar {jumlah}")
            print(f"penarikan berhasil. Saldo saat ini: {self.saldo}")
        else:
            print('Penarikan gagal. Cek saldo atau jumlah penarikan')

    #method untuk menampilkan saldo saat ini
    def cekSaldo(self):
        return self.saldo

# membuat objek akun1 dengna saldo awal 1000
akun1 = AkunBank('udin', 1000)

#melakukan beberapa transaksi
akun1.deposit(300)
akun1.tarik(500)
print('sisa saldo anda : ' , akun1.cekSaldo())