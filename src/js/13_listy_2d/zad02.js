/*
ZAD-02 — Macierz n×n: iloczyn indeksów

**Poziom:** ★☆☆
**Tagi:** `macierze`, `pętle zagnieżdżone`

### Treść

Wczytaj `n`. Utwórz i wypisz macierz `n×n`, gdzie element `[i][j]` (indeksy od 0) ma wartość `i*j`.

### Wejście

* 1. linia: `n`

### Wyjście

* `n` wierszy po `n` liczb

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
0 0 0
0 1 2
0 2 4
```

*/

// Funkcja tworzy kwadratową macierz n×n, gdzie element [i][j] = i*j
// Złożoność czasowa: O(n²), gdzie n to rozmiar macierzy
// Złożoność pamięciowa: O(n²)
function utworzMacierzKwadratowa(n) {
  const macierz = [];
  for (let i = 0; i < n; i++) {
    const wiersz = [];
    for (let j = 0; j < n; j++) {
      wiersz.push(i * j);
    }
    macierz.push(wiersz);
  }
  return macierz;
}

// test
function test() {
  const oczekiwana = [
    [0, 0, 0],
    [0, 1, 2],
    [0, 2, 4],
  ];
  const wynik = utworzMacierzKwadratowa(3);
  console.assert(
    wynik.length === oczekiwana.length,
    `Dlugosci macierzy nie sa rowne. Oczekiwano: ${oczekiwana.length}, otrzymano: ${wynik.length}.`
  );
  for (let i = 0; i < wynik.length; i++) {
    console.assert(
      wynik[i].length === oczekiwana[i].length,
      `Dlugosci wierszy nie sa rowne. Oczekiwano: ${oczekiwana[i].length}, otrzymano: ${wynik[i].length}.`
    );
    for (let j = 0; j < wynik[i].length; j++) {
      console.assert(
        wynik[i][j] === oczekiwana[i][j],
        `Element macierzy o indeksie (${i}, ${j}) nie jest taki sam jak w oczekiwanej macierzy. Oczekiwano: ${oczekiwana[i][j]}, otrzymano: ${wynik[i][j]}.`
      );
    }
  }
}

test();

