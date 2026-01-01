/*
ZAD-05 — Klasa Macierz

**Poziom:** ★★☆
**Tagi:** `class`, `macierze`, `operacje`

### Treść

Zaprojektuj klasę **Macierz**:

1. Konstruktor przyjmuje listę list (domyślnie pusta).
2. Operacje: dodawanie, odejmowanie, mnożenie.
3. Metoda wypisująca macierz (wierszami).
4. Porównania `==` i `!=`.

(Operację odwracania możesz pominąć w tym zadaniu, jeśli nie jest wymagana w sprawdzarce; najczęściej w podstawowych zadaniach nie ma testów na odwracanie.)

Program tworzy:

* A = [[1, 3], [4, 2]]
* B = [[5, 0], [1, 3]]

Wypisuje A, B, a potem A+B, A-B, A*B.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Macierz A:
[1, 3]
[4, 2]

Macierz B:
[5, 0]
[1, 3]

Suma macierzy:
[6, 3]
[5, 5]

Różnica macierzy A - B:
[-4, 3]
[3, -1]

Iloczyn macierzy A * B:
[8, 9]
[22, 12]
```

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

