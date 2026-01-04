/*
ZAD-09 — Klepsydra o największej sumie

**Poziom:** ★★☆
**Tagi:** `macierze`, `przeszukiwanie`

### Treść

Wczytaj macierz `n×m` (n,m ≥ 3). Znajdź maksymalną sumę „klepsydry” (7 pól):

```
a b c
  d
e f g
```

### Wejście

* 1. linia: `n m`
* następnie `n` wierszy po `m` liczb całkowitych

### Wyjście

* 1 linia: maksymalna suma klepsydry

### Przykład

**Wejście:**

```
4 4
7 4 2 0
4 8 10 8
3 6 7 6
3 9 19 14
```

**Wyjście:**

```
75
```

*/

function najwiekszaSumaKlepsydry(macierz) {
  const n = macierz.length;
  let najwiekszaSuma = 0;

  for (let i = 0; i <= n - 3; i++) {
    for (let j = 0; j <= n - 3; j++) {
      const suma =
        macierz[i][j] +
        macierz[i][j + 1] +
        macierz[i][j + 2] +
        macierz[i + 1][j + 1] +
        macierz[i + 2][j] +
        macierz[i + 2][j + 1] +
        macierz[i + 2][j + 2];

      if (suma > najwiekszaSuma) {
        najwiekszaSuma = suma;
      }
    }
  }

  return najwiekszaSuma;
}

// test
function test() {
  const macierz = [
    [7, 4, 2, 0],
    [4, 8, 10, 8],
    [3, 6, 7, 6],
    [3, 9, 19, 14],
  ];
  const wynik = 75;
  console.assert(
    najwiekszaSumaKlepsydry(macierz) === wynik,
    `Niepoprawny wynik dla macierzy ${macierz}.`
  );
}

test();

