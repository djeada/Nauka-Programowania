/*
ZAD-01 — Macierz z identycznymi wierszami 0..b

**Poziom:** ★☆☆
**Tagi:** `macierze`, `pętle`, `print`

### Treść

Wczytaj `a` i `b`. Wypisz macierz składającą się z `a` identycznych wierszy, gdzie każdy wiersz to liczby od `0` do `b` włącznie.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

* `a` wierszy, w każdym: `0 1 2 ... b`

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
0 1 2
0 1 2
0 1 2
```

*/

function utworzMacierz(a, b) {
  const macierz = [];
  for (let i = 0; i < a; i++) {
    const wiersz = [];
    for (let j = 0; j <= b; j++) {
      wiersz.push(j);
    }
    macierz.push(wiersz);
  }
  return macierz;
}

// test
function test() {
  const oczekiwana = [
    [0, 1, 2],
    [0, 1, 2],
    [0, 1, 2],
  ];
  const wynik = utworzMacierz(3, 2);
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

