/*

Tytul: Wywolywanie metody klasy bazowej w klasie potomnej

Tresc: Dla dwoch dowolnych klas, gdzie jedna jest klasa bazowa, a druga potomna, wywolaj metode klasy bazowej w metodzie klasy potomnej, ktora ja nadpisuje. Napisz program testujacy te klasy.
*/

class Zwierze {
  constructor(imie) {
    this.imie = imie;
  }

  dajGlos() {
    console.log("Jestem zwierzeciem!");
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
zwierze.dajGlos(); // wyswietli "Jestem zwierzeciem!"

const pies = new Pies("Burek");
pies.dajGlos(); // wyswietli "Jestem zwierzeciem!" oraz "Jestem psem!"

