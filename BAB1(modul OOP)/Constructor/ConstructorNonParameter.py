class Data:
    #no-argument parameter
    def __init__(self):
        self.nama = "Zahrul"
        self.alamat = "mayang"
    def show(self):
        print(f"nama {self.nama} alamat {self.alamat}")

nonpar = Data()
nonpar.show()  # Output: nama Zahrul alamat mayang