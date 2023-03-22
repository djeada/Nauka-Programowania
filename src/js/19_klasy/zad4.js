/*
Napisz klasy Wektor2D oraz Wektor3D reprezentujace odpowiednio 
wektory w przestrzeni dwuwymiarowej i trzywymiarowej. W sklad 
klas powinny wchodzic funkcje:
a) Konstruktor pobierajacy dwie (trzy) liczby jako argumenty. Liczby reprezentuja 
wspolrzedne wektora. Domyslne wartosci dla wszystkich argumentow wynosza 0.
b) Funkcje zwracajace wynik podstawowych operacji arytmetycznych (dodawanie, 
odejmowanie) oraz iloczyn wektorowy i skalarny. Jesli jest to mozliwe nalezy 
przeciazyc operatory: +, -, *.
c) Funkcja wypisujaca informacje o wektorze na standardowe wyjscie.
d) Funkcje umozliwiajace porownanie dwoch obiektow klasy Wektor2D(Wektor3D). Jesli 
jest to mozliwe nalezy przeciazyc operatory ==, !=.
e) Funkcja modul, zwracajaca modul wektora.
Napisz program testujacy twoja klase. Stworz wektory: A(-3, -3, -3) oraz B(5, 5, 5). 
Wypisz na standardowe wyjscie informacje o utworzonych wektorach oraz sume wektorow, 
roznice pierwszego i drugiego oraz ich iloczyn wektorowy.
*/

class Wektor2D {
  constructor(x, y) {
    this.x = x || 0;
    this.y = y || 0;
  }

  static dodaj(p1, p2) {
    return new Wektor2D(p1.x + p2.x, p1.y + p2.y);
  }

  static odejmij(p1, p2) {
    return new Wektor2D(p1.x - p2.x, p1.y - p2.y);
  }

  static iloczynWektorowy(p1, p2) {
    return p1.x * p2.x + p1.y * p2.y;
  }

  static iloczynSkalarny(p1, p2) {
    return p1.x * p2.y - p1.y * p2.x;
  }

  toString() {
    return `Wektor o wspolrzednych (${this.x}, ${this.y})`;
  }

  wypisz() {
    console.log(this.toString());
  }

  equals(p) {
    return this.x == p.x && this.y == p.y;
  }

  notEquals(p) {
    return !this.equals(p);
  }

  modul() {
    return Math.sqrt(Math.pow(this.x, 2) + Math.pow(this.y, 2));
  }
}

class Wektor3D extends Wektor2D {
  constructor(x, y, z) {
    super(x, y);
    this.z = z || 0;
  }

  static dodaj(p1, p2) {
    return new Wektor3D(p1.x + p2.x, p1.y + p2.y, p1.z + p2.z);
  }

  static odejmij(p1, p2) {
    return new Wektor3D(p1.x - p2.x, p1.y - p2.y, p1.z - p2.z);
  }

  static iloczynWektorowy(p1, p2) {
    return p1.x * p2.x + p1.y * p2.y + p1.z * p2.z;
  }

  static iloczynSkalarny(p1, p2) {
    return p1.x * p2.y - p1.y * p2.x;
  }

  toString() {
    return `Wektor o wspolrzednych (${this.x}, ${this.y}, ${this.z})`;
  }

  wypisz() {
    console.log(this.toString());
  }

  equals(p) {
    return this.x == p.x && this.y == p.y && this.z == p.z;
  }

  notEquals(p) {
    return !this.equals(p);
  }

  modul() {
    return Math.sqrt(
      Math.pow(this.x, 2) + Math.pow(this.y, 2) + Math.pow(this.z, 2)
    );
  }
}

main = function () {
  A = new Wektor3D(-3, -3, -3);
  B = new Wektor3D(5, 5, 5);

  console.log(`Wektor A: ${A.toString()}`);
  console.log(`Wektor B: ${B.toString()}`);
  console.log(`Suma wektorow: ${Wektor3D.dodaj(A, B).toString()}`);
  console.log(`Roznica wektorow: ${Wektor3D.odejmij(A, B).toString()}`);
  console.log(`Iloczyn wektorowy: ${Wektor3D.iloczynWektorowy(A, B)}`);
};

main();
