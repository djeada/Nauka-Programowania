/*

Tytul: Zaprojektuj klase Macierz.

Tresc: Napisz klase Macierz, ktora bedzie reprezentowala macierz. Klasa powinna zawierac nastepujace funkcje:

1. Konstruktor, ktory przyjmuje jako argument liste list liczb calkowitych. Pobrana lista reprezentuje macierz. Domyslna wartosc argumentu to pusta lista.
2. Funkcje, ktore zwracaja wynik podstawowych operacji arytmetycznych (dodawanie, odejmowanie, mnozenie) oraz odwracanie macierzy. Jesli jest to mozliwe, nalezy przeciazyc operatory: +, -, *.
3. Funkcje, ktora wypisuje informacje o macierzy na standardowe wyjscie.
4. Funkcje umozliwiajace porownanie dwoch obiektow klasy Macierz. Jesli jest to mozliwe, nalezy przeciazyc operatory == oraz !=.

Napisz program, ktory przetestuje twoja klase. Stworz macierze: A ([[1, 3], [4, 2]]) oraz B ([[5, 0], [1, 3]]). Wypisz na standardowe wyjscie informacje o utworzonych macierzach oraz ich sume, roznice pierwszej i drugiej oraz iloczyn macierzy.
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

