/*
ZAD-10 — Obróć macierz o 90° w prawo

**Poziom:** ★★☆
**Tagi:** `macierze`, `transpozycja`

### Treść

Wczytaj kwadratową macierz `n×n` i wypisz ją po obrocie o 90° zgodnie z ruchem wskazówek zegara.

### Wejście

* 1. linia: `n`
* następnie `n` wierszy po `n` liczb

### Wyjście

* `n` wierszy obróconej macierzy

### Przykład

**Wejście:**

```
3
1 2 3
4 5 6
7 8 9
```

**Wyjście:**

```
7 4 1
8 5 2
9 6 3
```

*/
// Funkcja obraca macierz kwadratową o 90° zgodnie z ruchem wskazówek zegara
// Złożoność czasowa: O(n²), gdzie n to rozmiar macierzy
// Złożoność pamięciowa: O(1) - modyfikacja in-place
function obrocMacierz(macierz) {
  const n = macierz.length;

  // Krok 1: Transpozycja macierzy (zamiana wierszy z kolumnami)
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      const temp = macierz[i][j];
      macierz[i][j] = macierz[j][i];
      macierz[j][i] = temp;
    }
  }

  // Krok 2: Odwrócenie kolejności elementów w każdym wierszu
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n / 2; j++) {
      const temp = macierz[i][j];
      macierz[i][j] = macierz[i][n - j - 1];
      macierz[i][n - j - 1] = temp;
    }
  }

  return macierz;
}

// test
function test() {
  const macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ];
  const wynik = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
  ];
  const wynikTestowy = obrocMacierz(macierz);
  let czyPoprawny = true;
  for (let i = 0; i < wynik.length; i++) {
    for (let j = 0; j < wynik[i].length; j++) {
      if (wynik[i][j] !== wynikTestowy[i][j]) {
        czyPoprawny = false;
        break;
      }
    }
  }
  if (czyPoprawny) {
    console.log("Test przeszedl pomyslnie");
  } else {
    console.error("Niepoprawny wynik dla macierzy ", macierz);
  }
}

test();

