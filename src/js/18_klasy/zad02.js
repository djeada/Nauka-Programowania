/*
ZAD-02 — Klasa Punkt

**Poziom:** ★★☆
**Tagi:** `class`, `static`, `porównania`, `math`

### Treść

Zaprojektuj klasę **Punkt**:

1. Konstruktor `(x=0, y=0)`.
2. Metoda statyczna `odleglosc(p1, p2)` licząca odległość.
3. Metoda wypisująca współrzędne.
4. Porównania `==` i `!=` (równe, gdy oba współrzędne identyczne).

Program tworzy:

* A = (5, 5)
* B = (-3, -3)

Wypisuje oba punkty i odległość między nimi (4 miejsca po przecinku).

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Punkt A: (5, 5)
Punkt B: (-3, -3)
Odległość między punktami A i B: 11.3137
```

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

