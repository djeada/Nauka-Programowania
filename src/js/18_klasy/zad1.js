/*

Tytuł: Zaprojektuj klasę Koło.

Opis zadania: Napisz klasę Koło, która będzie reprezentowała koło. Klasa powinna zawierać następujące funkcje:

1. Konstruktor, który przyjmuje jedną liczbę jako argument, reprezentującą promień koła. Domyślną wartością promienia powinno być 1.
2. Funkcję obwód, która zwraca obwód koła.
3. Funkcję pole, która zwraca pole koła.
4. Funkcję, która wypisuje informacje o kole na standardowe wyjście.

Napisz program, który przetestuje twoją klasę. Stwórz koło o promieniu 3 i użyj funkcji wypisującej informacje o kole.
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
      `Koło o promieniu ${
        this.promien
      }, obwód: ${this.obwod()}, pole: ${this.pole()}`
    );
  }
}

const mojeKolo = new Kolo(3);
mojeKolo.wypiszInfo();
