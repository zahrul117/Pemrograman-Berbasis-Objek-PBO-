class Karakter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

pahlawan = Karakter('Udin', 999)

print(f"nama karakter : {pahlawan.name}")
print(f'Levek karakter : {pahlawan.level}')