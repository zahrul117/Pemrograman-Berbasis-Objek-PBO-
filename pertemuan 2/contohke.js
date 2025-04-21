class Rumah {
  constructor(bahan, harga, lokasi, model) {
    this.bahan = bahan;
    this.harga = harga;
    this.lokasi = lokasi;
    this.model = model;
  }
  show() {
    console.log(`Bahan bangunan ${this.bahan} Berharga ${this.harga}`);
  }

  gaya() {
    console.log(`Rumah Idamanku ${this.model} dan lokasinya di ${this.lokasi}`);
  }
}

const rumah1 = new Rumah("Kayu", 700000000, "perdesaan", "Britania Clasic");
const rumah2 = new Rumah("Beton", 1500000000, "Perkotaan", "Clasic Modern");

rumah1.show();
rumah1.gaya();
console.log("========================================");
rumah2.show();
rumah2.gaya();
