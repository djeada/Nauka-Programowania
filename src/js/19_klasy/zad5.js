/*
Napisz klase Macierz reprezentujaca macierz. W sklad klasy powinny wchodzic funkcje:
a) Konstruktor pobierajacy liste list liczb calkowitych. Pobrana lista reprezentuje macierz. 
Domyslna wartosc argumentu to pusta lista.
b) Funkcje zwracajace wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie, mnozenie) 
oraz odwracanie macierzy. Jesli jest to mozliwe nalezy przeciazyc operatory: +, -, *.
c) Funkcja wypisujaca informacje o macierzy na standardowe wyjscie.
d) Funkcje umozliwiajace porownanie dwoch obiektow klasy Macierz. Jesli jest to mozliwe nalezy 
przeciazyc operatory ==, !=.
Napisz program testujacy twoja klase. Stworz macierze: A([[1, 3], [4, 2]]) i B([[5, 0], [1, 3]]). 
Wypisz na standardowe wyjscie informacje o utworzonych macierzach oraz ich sume, roznice pierwszej 
i drugiej oraz iloczyn macierzy. 
*/

class Macierz {
  constructor(lista) {
    this.lista = lista || [];
  }

  odwrotna() {
    let lista = [];
    for (let i = 0; i < this.lista.length; i++) {
      let lista2 = [];
      for (let j = 0; j < this.lista[i].length; j++) {
        lista2.push(this.lista[j][i]);
      }
      lista.push(lista2);
    }
    return new Macierz(lista);
  }

  wypisz() {
    console.log(this.toString());
  }

  toString() {
    return "\n" + this.lista.map((row) => row.join(" ")).join("\n") + "\n";
  }

  equals(m2) {
    if (this.lista.length != m2.lista.length) {
      return false;
    }
    for (let i = 0; i < this.lista.length; i++) {
      if (this.lista[i].length != m2.lista[i].length) {
        return false;
      }
      for (let j = 0; j < this.lista[i].length; j++) {
        if (this.lista[i][j] != m2.lista[i][j]) {
          return false;
        }
      }
    }
    return true;
  }

  notEquals(m2) {
    return !this.equals(m2);
  }

  static dodaj(m1, m2) {
    let lista = [];
    for (let i = 0; i < m1.lista.length; i++) {
      let lista2 = [];
      for (let j = 0; j < m1.lista[i].length; j++) {
        lista2.push(m1.lista[i][j] + m2.lista[i][j]);
      }
      lista.push(lista2);
    }
    return new Macierz(lista);
  }

  static odejmij(m1, m2) {
    let lista = [];
    for (let i = 0; i < m1.lista.length; i++) {
      let lista2 = [];
      for (let j = 0; j < m1.lista[i].length; j++) {
        lista2.push(m1.lista[i][j] - m2.lista[i][j]);
      }
      lista.push(lista2);
    }
    return new Macierz(lista);
  }

  static mnozenie(m1, m2) {
    let lista = [];
    for (let i = 0; i < m1.lista.length; i++) {
      let lista2 = [];
      for (let j = 0; j < m1.lista[i].length; j++) {
        let suma = 0;
        for (let k = 0; k < m1.lista[i].length; k++) {
          suma += m1.lista[i][k] * m2.lista[k][j];
        }
        lista2.push(suma);
      }
      lista.push(lista2);
    }
    return new Macierz(lista);
  }
}

main = function () {
  A = new Macierz([
    [1, 3],
    [4, 2],
  ]);
  B = new Macierz([
    [5, 0],
    [1, 3],
  ]);

  console.log(`Macierz A: ${A.toString()}`);
  console.log(`Macierz B: ${B.toString()}`);

  console.log(`Suma A+B: ${Macierz.dodaj(A, B).toString()}`);
  console.log(`Roznica A-B: ${Macierz.odejmij(A, B).toString()}`);
  console.log(`Iloczyn A*B: ${Macierz.mnozenie(A, B).toString()}`);
  console.log(`Odwrotna A: ${A.odwrotna().toString()}`);

  console.log(`Czy A==B? ${A.equals(B)}`);
  console.log(`Czy A!=B? ${A.notEquals(B)}`);
};

main();
