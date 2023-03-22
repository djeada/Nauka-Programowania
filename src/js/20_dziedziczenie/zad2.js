/*
Zaprojektuj klase Ksztalt oraz klasy pochodne Kolo i Kwadrat.
*/

class Ksztalt {
  pole() {
    throw new Error(
      `Nie zaimplementowano metody pole() w klasie ${this.constructor.name}`
    );
  }

  obwod() {
    throw new Error(
      `Nie zaimplementowano metody obwod() w klasie ${this.constructor.name}`
    );
  }

  wypisz() {
    console.log(`Obwod ${this.constructor.name} wynosi ${this.obwod()}`);
    console.log(`Pole ${this.constructor.name} wynosi ${this.pole()}`);
  }
}

class Kolo extends Ksztalt {
  constructor(promien) {
    super();
    this.promien = promien;
  }

  pole() {
    return Math.PI * this.promien * this.promien;
  }

  obwod() {
    return 2 * Math.PI * this.promien;
  }
}

class Kwadrat extends Ksztalt {
  constructor(bok) {
    super();
    this.bok = bok;
  }

  pole() {
    return this.bok * this.bok;
  }

  obwod() {
    return 4 * this.bok;
  }
}

main = function () {
  let kolo = new Kolo(3);
  kolo.wypisz();

  let kwadrat = new Kwadrat(3);
  kwadrat.wypisz();
};

main();
