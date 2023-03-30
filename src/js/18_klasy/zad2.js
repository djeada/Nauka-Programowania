/*

Tytul: Zaprojektuj klase Punkt.

Tresc: Napisz klase Punkt, ktora bedzie reprezentowala punkt w ukladzie kartezjanskim. Klasa powinna zawierac nastepujace funkcje:

1. Konstruktor, ktory przyjmuje dwa argumenty (liczby). Pierwsza liczba reprezentuje wspolrzedna x, a druga wspolrzedna y. Domyslne wartosci dla obu argumentow powinny wynosic 0.
2. Funkcje statyczna odleglosc, ktora zwraca odleglosc miedzy dwoma punktami (obiektami klasy Punkt).
3. Funkcje, ktora wypisuje informacje o punkcie na standardowe wyjscie.
4. Funkcje umozliwiajace porownanie dwoch obiektow klasy Punkt. Jesli jest to mozliwe, nalezy przeciazyc operatory == oraz !=.

Napisz program, ktory przetestuje twoja klase. Stworz punkty: A (5, 5) oraz B (-3, -3). Wypisz na standardowe wyjscie informacje o utworzonych punktach oraz odleglosc miedzy nimi.
*/

class Punkt {
  constructor(x = 0, y = 0) {
    this.x = x;
    this.y = y;
  }

  static odleglosc(punkt1, punkt2) {
    const dx = punkt1.x - punkt2.x;
    const dy = punkt1.y - punkt2.y;
    return Math.sqrt(dx ** 2 + dy ** 2);
  }

  wypiszInfo() {
    console.log(`Punkt (${this.x}, ${this.y})`);
  }

  equals(other) {
    return this.x === other.x && this.y === other.y;
  }

  notEquals(other) {
    return !this.equals(other);
  }

  static fromArray([x = 0, y = 0]) {
    return new Punkt(x, y);
  }
}

const punktA = new Punkt(5, 5);
const punktB = new Punkt(-3, -3);

punktA.wypiszInfo();
punktB.wypiszInfo();

const odlegloscAB = Punkt.odleglosc(punktA, punktB);
console.log(`Odleglosc miedzy punktem A i B: ${odlegloscAB}`);

