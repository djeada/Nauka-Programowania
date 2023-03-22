/*

Tytuł: Wywoływanie metody klasy bazowej w klasie potomnej

Treść: Dla dwóch dowolnych klas, gdzie jedna jest klasą bazową, a druga potomną, wywołaj metodę klasy bazowej w metodzie klasy potomnej, która ją nadpisuje. Napisz program testujący te klasy.
*/

class Zwierze {
  constructor(imie) {
    this.imie = imie;
  }

  dajGlos() {
    console.log("Jestem zwierzęciem!");
  }
}

class Pies extends Zwierze {
  constructor(imie) {
    super(imie);
  }

  dajGlos() {
    super.dajGlos();
    console.log("Jestem psem!");
  }
}

const zwierze = new Zwierze("Bajka");
zwierze.dajGlos(); // wyświetli "Jestem zwierzęciem!"

const pies = new Pies("Burek");
pies.dajGlos(); // wyświetli "Jestem zwierzęciem!" oraz "Jestem psem!"
