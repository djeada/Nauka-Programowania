/*

Tytul: Zaprojektuj klase Kolo.

Opis zadania: Napisz klase Kolo, ktora bedzie reprezentowala kolo. Klasa powinna zawierac nastepujace funkcje:

1. Konstruktor, ktory przyjmuje jedna liczbe jako argument, reprezentujaca promien kola. Domyslna wartoscia promienia powinno byc 1.
2. Funkcje obwod, ktora zwraca obwod kola.
3. Funkcje pole, ktora zwraca pole kola.
4. Funkcje, ktora wypisuje informacje o kole na standardowe wyjscie.

Napisz program, ktory przetestuje twoja klase. Stworz kolo o promieniu 3 i uzyj funkcji wypisujacej informacje o kole.
*/

class Kolo {
  constructor(promien = 1) {
    this.promien = promien;
  }

  obwod() {
    return 2 * Math.PI * this.promien;
  }

  pole() {
    return Math.PI * this.promien ** 2;
  }

  wypiszInfo() {
    console.log(
      `Kolo o promieniu ${
        this.promien
      }, obwod: ${this.obwod()}, pole: ${this.pole()}`
    );
  }
}

const mojeKolo = new Kolo(3);
mojeKolo.wypiszInfo();

