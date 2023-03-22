/*
Tytuł: Zaprojektuj klasę Kształt oraz klasy potomne Koło i Kwadrat.

Treść: Zaprojektuj klasę Kształt oraz klasy potomne Koło i Kwadrat. Napisz program testujący te klasy.
*/
class Kształt {
  pobierzNazwe() {
    return "Kształt";
  }
}

class Koło extends Kształt {
  constructor(promien) {
    super();
    this.promien = promien;
  }

  pobierzNazwe() {
    return "Koło";
  }

  pobierzPole() {
    return Math.PI * this.promien * this.promien;
  }

  pobierzObwod() {
    return 2 * Math.PI * this.promien;
  }
}

class Kwadrat extends Kształt {
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

const kolo = new Koło(5);
console.log(kolo.pobierzNazwe()); // wyświetli "Koło"
console.log(kolo.pobierzPole()); // wyświetli 78.53981633974483
console.log(kolo.pobierzObwod()); // wyświetli 31.41592653589793

const kwadrat = new Kwadrat(4);
console.log(kwadrat.pobierzNazwe()); // wyświetli "Kwadrat"
console.log(kwadrat.pobierzPole()); // wyświetli 16
console.log(kwadrat.pobierzObwod()); // wyświetli 16
