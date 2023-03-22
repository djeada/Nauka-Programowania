/*
Napisz klase Kolo reprezentujaca kolo. W sklad klasy powinny wchodzic funkcje:
a) Konstruktor pobierajacy jedna liczbe jako argument, reprezentujaca promien kola. Domyslna wartosc promienia to 1.
b) Funkcja obwod, zwracajaca obwod kola.
c) Funkcja pole, zwracajaca pole kola.
d) Funkcja wypisujaca informacje o kole na standardowe wyjscie.
Napisz program testujacy twoja klase. Stworz kolo o promieniu rownym 3 i uzyj funkcji wypisujacej informacje o kole.
*/

class Kolo {
  constructor(promien) {
    this.promien = promien || 1;
  }

  obwod() {
    return 2 * Math.PI * this.promien;
  }

  pole() {
    return Math.PI * this.promien * this.promien;
  }

  wypisz() {
    console.log(
      `Obwod kola o promieniu ${this.promien} wynosi ${this.obwod()}`
    );
    console.log(`Pole kola o promieniu ${this.promien} wynosi ${this.pole()}`);
  }
}

main = function () {
  let kolo = new Kolo(3);
  kolo.wypisz();
};

main();
