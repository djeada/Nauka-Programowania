/*

Tytul: Zaprojektuj klasy Wektor2D oraz Wektor3D.

Tresc:  Napisz klasy Wektor2D oraz Wektor3D, ktore beda reprezentowaly odpowiednio wektory w przestrzeni dwuwymiarowej i trzywymiarowej. Klasy powinny zawierac nastepujace funkcje:

1. Konstruktor, ktory przyjmuje dwa (trzy) argumenty (liczby). Liczby reprezentuja wspolrzedne wektora. Domyslne wartosci dla wszystkich argumentow powinny wynosic 0.
2. Funkcje, ktore zwracaja wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie) oraz iloczyn wektorowy i skalarny. Jesli jest to mozliwe, nalezy przeciazyc operatory: +, -, *.
3. Funkcje, ktora wypisuje informacje o wektorze na standardowe wyjscie.
4. Funkcje umozliwiajace porownanie dwoch obiektow klasy Wektor2D (Wektor3D). Jesli jest to mozliwe, nalezy przeciazyc operatory == oraz !=.
5. Funkcje modul, ktora zwraca modul wektora.

Napisz program, ktory przetestuje twoja klase. Stworz wektory: A (-3, -3, -3) oraz B (5, 5, 5). Wypisz na standardowe wyjscie informacje o utworzonych wektorach oraz sume wektorow, roznice pierwszego i drugiego oraz ich iloczyn wektorowy.
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

