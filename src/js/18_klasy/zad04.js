/*
ZAD-04 — Klasy Wektor2D i Wektor3D

**Poziom:** ★★☆
**Tagi:** `class`, `operatory`, `math`

### Treść

Zaprojektuj klasy **Wektor2D** i **Wektor3D**:

Wspólne:

* konstruktor z domyślnymi współrzędnymi 0,
* dodawanie, odejmowanie,
* iloczyn skalarny,
* porównania `==` i `!=`,
* moduł (długość),
* metoda wypisująca wektor.

Dodatkowo dla **Wektor3D**:

* iloczyn wektorowy.

Program tworzy:

* A = (-3, -3, -3)
* B = (5, 5, 5)

Wypisuje A, B oraz:

* A + B
* A - B
* A · B
* A × B

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Wektor A: (-3, -3, -3)
Wektor B: (5, 5, 5)
Suma wektorów: (2, 2, 2)
Różnica wektorów A - B: (-8, -8, -8)
Iloczyn skalarny: -45
Iloczyn wektorowy: (0, 0, 0)
```

*/

class Wektor2D {
  constructor(x = 0, y = 0) {
    this.x = x;
    this.y = y;
  }

  dodaj(innyWektor) {
    return new Wektor2D(this.x + innyWektor.x, this.y + innyWektor.y);
  }

  odejmij(innyWektor) {
    return new Wektor2D(this.x - innyWektor.x, this.y - innyWektor.y);
  }

  mnoz(skalar) {
    return new Wektor2D(this.x * skalar, this.y * skalar);
  }

  iloczynWektorowy(innyWektor) {
    return this.x * innyWektor.y - this.y * innyWektor.x;
  }

  iloczynSkalarny(innyWektor) {
    return this.x * innyWektor.x + this.y * innyWektor.y;
  }

  wypiszInfo() {
    console.log(`Wektor (${this.x}, ${this.y})`);
  }

  equals(other) {
    return this.x === other.x && this.y === other.y;
  }

  notEquals(other) {
    return !this.equals(other);
  }

  modul() {
    return Math.sqrt(this.x ** 2 + this.y ** 2);
  }

  static fromArray([x = 0, y = 0]) {
    return new Wektor2D(x, y);
  }
}

class Wektor3D extends Wektor2D {
  constructor(x = 0, y = 0, z = 0) {
    super(x, y);
    this.z = z;
  }

  dodaj(innyWektor) {
    return new Wektor3D(
      this.x + innyWektor.x,
      this.y + innyWektor.y,
      this.z + innyWektor.z
    );
  }

  odejmij(innyWektor) {
    return new Wektor3D(
      this.x - innyWektor.x,
      this.y - innyWektor.y,
      this.z - innyWektor.z
    );
  }

  mnoz(skalar) {
    return new Wektor3D(this.x * skalar, this.y * skalar, this.z * skalar);
  }

  iloczynWektorowy(innyWektor) {
    const x = this.y * innyWektor.z - this.z * innyWektor.y;
    const y = this.z * innyWektor.x - this.x * innyWektor.z;
    const z = this.x * innyWektor.y - this.y * innyWektor.x;
    return new Wektor3D(x, y, z);
  }

  iloczynSkalarny(innyWektor) {
    return (
      this.x * innyWektor.x + this.y * innyWektor.y + this.z * innyWektor.z
    );
  }

  wypiszInfo() {
    console.log(`Wektor (${this.x}, ${this.y}, ${this.z})`);
  }

  equals(other) {
    return this.x === other.x && this.y === other.y && this.z === other.z;
  }

  notEquals(other) {
    return !this.equals(other);
  }

  modul() {
    return Math.sqrt(this.x ** 2 + this.y ** 2 + this.z ** 2);
  }

  static fromArray([x = 0, y = 0, z = 0]) {
    return new Wektor3D(x, y, z);
  }

  static fromWektor2D(wektor2D, z = 0) {
    return new Wektor3D(wektor2D.x, wektor2D.y, z);
  }
}

const wektorA = new Wektor3D(-3, -3, -3);
const wektorB = new Wektor3D(5, 5, 5);

wektorA.wypiszInfo();
wektorB.wypiszInfo();

const suma = wektorA.dodaj(wektorB);
const roznica = wektorA.odejmij(wektorB);
const iloczynWektorowy = wektorA.iloczynWektorowy(wektorB);
const iloczynSkalarny = wektorA.iloczynSkalarny(wektorB);

suma.wypiszInfo();
roznica.wypiszInfo();
iloczynWektorowy.wypiszInfo();
console.log(iloczynSkalarny);

