/*

Tytuł: Zaprojektuj klasę Punkt.

Treść: Napisz klasę Punkt, która będzie reprezentowała punkt w układzie kartezjańskim. Klasa powinna zawierać następujące funkcje:

1. Konstruktor, który przyjmuje dwa argumenty (liczby). Pierwsza liczba reprezentuje współrzędną x, a druga współrzędną y. Domyślne wartości dla obu argumentów powinny wynosić 0.
2. Funkcję statyczną odległość, która zwraca odległość między dwoma punktami (obiektami klasy Punkt).
3. Funkcję, która wypisuje informacje o punkcie na standardowe wyjście.
4. Funkcje umożliwiające porównanie dwóch obiektów klasy Punkt. Jeśli jest to możliwe, należy przeciążyć operatory == oraz !=.

Napisz program, który przetestuje twoją klasę. Stwórz punkty: A (5, 5) oraz B (-3, -3). Wypisz na standardowe wyjście informacje o utworzonych punktach oraz odległość między nimi.
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
console.log(`Odległość między punktem A i B: ${odlegloscAB}`);
