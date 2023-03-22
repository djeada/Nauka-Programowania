/*
Napisz klase Punkt reprezentujaca punkt w ukladzie kartezjanskim. W sklad klasy powinny wchodzic funkcje:
a) Konstruktor pobierajacy dwie liczby jako argumenty. Pierwsza liczba reprezentuje wspolrzedna x, a druga 
wspolrzedna y. Domyslne wartosci dla obu argumentow wynosza 0.
b) Funkcja statyczna odleglosc, zwracajaca odleglosc miedzy dwoma punktami (obiektami klasy Punkt).
c) Funkcja wypisujaca informacje o punkcie na standardowe wyjscie.
d) Funkcje umozliwiajace porownanie dwoch obiektow klasy Punkt. Jesli jest to mozliwe nalezy przeciazyc 
operatory ==, !=.
Napisz program testujacy twoja klase. Stworz punkty: A(5, 5) oraz B(-3, -3). Wypisz na standardowe wyjscie 
informacje o utworzonych punktach oraz odleglosc miedzy nimi.
*/

class Punkt {
  constructor(x, y) {
    this.x = x || 0;
    this.y = y || 0;
  }

  static odleglosc(p1, p2) {
    return Math.sqrt(Math.pow(p1.x - p2.x, 2) + Math.pow(p1.y - p2.y, 2));
  }

  wypisz() {
    console.log(`Punkt o wspolrzednych (${this.x}, ${this.y})`);
  }

  equals(p) {
    return this.x == p.x && this.y == p.y;
  }

  notEquals(p) {
    return !this.equals(p);
  }
}

main = function () {
  let p1 = new Punkt(5, 5);
  let p2 = new Punkt(-3, -3);
  console.log(
    `Odleglosc miedzy punktami ${p1.wypisz()} i ${p2.wypisz()} wynosi ${Punkt.odleglosc(
      p1,
      p2
    )}`
  );
};

main();
