class Kotak {
  constructor(nama) {
    this.nama = nama;
  }

  tampilkan() {
    console.log(`Ini adalah ${this.nama}`);
  }
}

class Kubus extends Kotak {
  kubusInfo() {
    console.log("Kubus punya 6 sisi yang sama panjang.");
  }
}

class Balok extends Kotak {
  balokInfo() {
    console.log("Balok memiliki panjang, lebar, dan tinggi yang berbeda.");
  }
}

class Kerucut extends Kotak {
  kerucutInfo() {
    console.log("Kerucut memiliki alas lingkaran dan satu titik puncak.");
  }
}

// Membuat objek
const kotak1 = new Kubus("Kubus");
const kotak2 = new Balok("Balok");
const kotak3 = new Kerucut("Kerucut");

// Memanggil method dari parent dan method khusus
kotak1.tampilkan();
kotak1.kubusInfo();

kotak2.tampilkan();
kotak2.balokInfo();

kotak3.tampilkan();
kotak3.kerucutInfo();
