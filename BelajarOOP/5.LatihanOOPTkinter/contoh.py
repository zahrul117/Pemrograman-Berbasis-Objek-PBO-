import tkinter as tk

class AplikasiBuku:
    def __init__(self, master):
        self.master = master
        master.title("Input Buku")

        # Label
        self.label_judul = tk.Label(master, text="Judul Buku:")
        self.label_judul.grid(row=0, column=0)

        self.label_pengarang = tk.Label(master, text="Pengarang:")
        self.label_pengarang.grid(row=1, column=0)

        # Entry
        self.entry_judul = tk.Entry(master)
        self.entry_judul.grid(row=0, column=1)

        self.entry_pengarang = tk.Entry(master)
        self.entry_pengarang.grid(row=1, column=1)

        # Tombol
        self.tombol_tampil = tk.Button(master, text="Tampilkan", command=self.tampilkan_buku)
        self.tombol_tampil.grid(row=2, column=0, columnspan=2)

        # Output Label
        self.output = tk.Label(master, text="", fg="blue")
        self.output.grid(row=3, column=0, columnspan=2)

    def tampilkan_buku(self):
        judul = self.entry_judul.get()
        pengarang = self.entry_pengarang.get()
        self.output.config(text=f"Buku: {judul} | Pengarang: {pengarang}")

# Jalankan aplikasi
root = tk.Tk()
app = AplikasiBuku(root)
root.mainloop()
