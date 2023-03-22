/*

Tytuł: Zaprojektuj klasę Macierz.

Treść: Napisz klasę Macierz, która będzie reprezentowała macierz. Klasa powinna zawierać następujące funkcje:

1. Konstruktor, który przyjmuje jako argument listę list liczb całkowitych. Pobrana lista reprezentuje macierz. Domyślna wartość argumentu to pusta lista.
2. Funkcje, które zwracają wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie, mnożenie) oraz odwracanie macierzy. Jeśli jest to możliwe, należy przeciążyć operatory: +, -, *.
3. Funkcję, która wypisuje informacje o macierzy na standardowe wyjście.
4. Funkcje umożliwiające porównanie dwóch obiektów klasy Macierz. Jeśli jest to możliwe, należy przeciążyć operatory == oraz !=.

Napisz program, który przetestuje twoją klasę. Stwórz macierze: A ([[1, 3], [4, 2]]) oraz B ([[5, 0], [1, 3]]). Wypisz na standardowe wyjście informacje o utworzonych macierzach oraz ich sumę, różnicę pierwszej i drugiej oraz iloczyn macierzy.
*/

class Macierz {
  constructor(lista = []) {
    this.lista = lista;
  }

  dodaj(innaMacierz) {
    const result = [];
    for (let i = 0; i < this.lista.length; i++) {
      const row = [];
      for (let j = 0; j < this.lista[i].length; j++) {
        row.push(this.lista[i][j] + innaMacierz.lista[i][j]);
      }
      result.push(row);
    }
    return new Macierz(result);
  }

  odejmij(innaMacierz) {
    const result = [];
    for (let i = 0; i < this.lista.length; i++) {
      const row = [];
      for (let j = 0; j < this.lista[i].length; j++) {
        row.push(this.lista[i][j] - innaMacierz.lista[i][j]);
      }
      result.push(row);
    }
    return new Macierz(result);
  }

  pomnoz(innaMacierz) {
    const result = [];
    for (let i = 0; i < this.lista.length; i++) {
      const row = [];
      for (let j = 0; j < innaMacierz.lista[0].length; j++) {
        let sum = 0;
        for (let k = 0; k < innaMacierz.lista.length; k++) {
          sum += this.lista[i][k] * innaMacierz.lista[k][j];
        }
        row.push(sum);
      }
      result.push(row);
    }
    return new Macierz(result);
  }

  odwroc() {
    const n = this.lista.length;
    const augmented = this.lista.map((row, i) =>
      row.concat(Array(n).fill(i === n - 1 ? 1 : 0))
    );
    for (let i = 0; i < n; i++) {
      let maxRow = i;
      for (let j = i + 1; j < n; j++) {
        if (Math.abs(augmented[j][i]) > Math.abs(augmented[maxRow][i])) {
          maxRow = j;
        }
      }
      [augmented[i], augmented[maxRow]] = [augmented[maxRow], augmented[i]];
      for (let j = i + 1; j < n; j++) {
        const coef = -augmented[j][i] / augmented[i][i];
        for (let k = i; k < 2 * n; k++) {
          augmented[j][k] += coef * augmented[i][k];
        }
      }
    }
    for (let i = n - 1; i >= 0; i--) {
      for (let j = i - 1; j >= 0; j--) {
        const coef = -augmented[j][i] / augmented[i][i];
        for (let k = i; k < 2 * n; k++) {
          augmented[j][k] += coef * augmented[i][k];
        }
      }
      const coef = 1 / augmented[i][i];
      for (let k = i; k < 2 * n; k++) {
        augmented[i][k] *= coef;
      }
    }
    return new Macierz(augmented.map((row) => row.slice(n)));
  }

  wypiszInfo() {
    console.log(`Macierz ${this.lista.length}x${this.lista[0].length}:`);
    for (let i = 0; i < this.lista.length; i++) {
      console.log(this.lista[i].join(" "));
    }
  }

  porownaj(innaMacierz) {
    if (this.lista.length !== innaMacierz.lista.length) {
      return false;
    }
    for (let i = 0; i < this.lista.length; i++) {
      if (this.lista[i].length !== innaMacierz.lista[i].length) {
        return false;
      }
      for (let j = 0; j < this.lista[i].length; j++) {
        if (this.lista[i][j] !== innaMacierz.lista[i][j]) {
          return false;
        }
      }
    }
    return true;
  }
}

const A = new Macierz([
  [1, 3],
  [4, 2],
]);
const B = new Macierz([
  [5, 0],
  [1, 3],
]);
A.wypiszInfo();
B.wypiszInfo();

const suma = A.dodaj(B);
suma.wypiszInfo();

const roznica = A.odejmij(B);
roznica.wypiszInfo();

const iloczyn = A.pomnoz(B);
iloczyn.wypiszInfo();

const odwrocona = A.odwroc();
odwrocona.wypiszInfo();

console.log(A.porownaj(B));
console.log(A.porownaj(A));
