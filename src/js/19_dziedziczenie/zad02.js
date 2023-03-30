/*
Tytul: Zaprojektuj klase Ksztalt oraz klasy potomne Kolo i Kwadrat.

Tresc: Zaprojektuj klase Ksztalt oraz klasy potomne Kolo i Kwadrat. Napisz program testujacy te klasy.
*/
class Ksztalt {
  pobierzNazwe() {
    return "Ksztalt";
  }
}

class Kolo extends Ksztalt {
  constructor(promien) {
    super();
    this.promien = promien;
  }

  pobierzNazwe() {
    return "Kolo";
  }

  pobierzPole() {
    return Math.PI * this.promien * this.promien;
  }

  pobierzObwod() {
    return 2 * Math.PI * this.promien;
  }
}

class Kwadrat extends Ksztalt {
  constructor(bok) {
    super();
    this.bok = bok;
  }

  pobierzNazwe() {
    return "Kwadrat";
  }

  pobierzPole() {
    return this.bok * this.bok;
  }

  pobierzObwod() {
    return 4 * this.bok;
  }
}

const kolo = new Kolo(5);
console.log(kolo.pobierzNazwe()); // wyswietli "Kolo"
console.log(kolo.pobierzPole()); // wyswietli 78.53981633974483
console.log(kolo.pobierzObwod()); // wyswietli 31.41592653589793

const kwadrat = new Kwadrat(4);
console.log(kwadrat.pobierzNazwe()); // wyswietli "Kwadrat"
console.log(kwadrat.pobierzPole()); // wyswietli 16
console.log(kwadrat.pobierzObwod()); // wyswietli 16

