class Person {
  constructor(name, sex, profession) {
    this.name = name;
    this.sex = sex;
    this.profession = profession;
  }
  show() {
    console.log(
      `Name : ${this.name}, jenis kelamin : ${this.sex}, pekerjaan : ${this.profession}`
    );
  }
  work() {
    console.log(`${this.name} sedang bekerja sebagai ${this.profession}`);
  }
}

zahrul = new Person("Zahrul", "Jantan", "Back-end");
zahrul.show();
zahrul.work();
