/*
ZAD-05 — Czy macierz jest magiczna?

**Poziom:** ★★☆
**Tagi:** `macierze`, `suma`, `warunki`

### Treść

Wczytaj macierz kwadratową `n×n` z dodatnimi liczbami naturalnymi. Sprawdź, czy to **kwadrat magiczny**: suma każdego wiersza, każdej kolumny oraz obu przekątnych jest taka sama.

### Wejście

* 1. linia: `n`
* następnie `n` wierszy po `n` liczb

### Wyjście

* `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
3
6 7 2
1 5 9
8 3 4
```

**Wyjście:**

```
Prawda
```

*/

// Funkcja sprawdza czy macierz jest kwadratem magicznym
// (sumy wierszy, kolumn i przekątnych są równe)
// Złożoność czasowa: O(n²), gdzie n to rozmiar macierzy
// Złożoność pamięciowa: O(1)
function czyKwadratMagiczny(macierz) {
  const n = macierz.length;
  const sumaOczekiwana = (n * (n * n + 1)) / 2;
  let sumaWiersza,
    sumaKolumny,
    sumaPrzekatnej1 = 0,
    sumaPrzekatnej2 = 0;
  for (let i = 0; i < n; i++) {
    sumaWiersza = 0;
    sumaKolumny = 0;
    for (let j = 0; j < n; j++) {
      sumaWiersza += macierz[i][j];
      sumaKolumny += macierz[j][i];
      if (i === j) {
        sumaPrzekatnej1 += macierz[i][j];
      }
      if (i + j === n - 1) {
        sumaPrzekatnej2 += macierz[i][j];
      }
    }
    if (sumaWiersza !== sumaOczekiwana || sumaKolumny !== sumaOczekiwana) {
      return false;
    }
  }
  if (
    sumaPrzekatnej1 !== sumaOczekiwana ||
    sumaPrzekatnej2 !== sumaOczekiwana
  ) {
    return false;
  }
  return true;
}

// test
function test() {
  const macierz1 = [
    [6, 7, 2],
    [1, 5, 9],
    [8, 3, 4],
  ];
  const wynik1 = true;
  const macierz2 = [
    [6, 7, 2],
    [1, 5, 9],
    [8, 3, 3],
  ];
  const wynik2 = false;
  console.assert(
    czyKwadratMagiczny(macierz1) === wynik1,
    `Macierz ${macierz1} nie jest kwadratem magicznym, a powinna byc.`
  );
  console.assert(
    czyKwadratMagiczny(macierz2) === wynik2,
    `Macierz ${macierz2} jest kwadratem magicznym, a nie powinna byc.`
  );
}

test();

