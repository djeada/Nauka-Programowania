/*
ZAD-07 — Zamiana sąsiadujących bitów

**Poziom:** ★☆☆
**Tagi:** `bitwise`, `maski`, `swap bits`

### Treść

Wczytaj liczbę naturalną `n`. Zamień miejscami każdą parę sąsiadujących bitów w jej zapisie binarnym:

* bit 0 z bitem 1,
* bit 2 z bitem 3,
* bit 4 z bitem 5,
* itd.

Następnie wypisz wynik w systemie dziesiętnym.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: wynik po zamianie bitów.

### Przykład

**Wejście:**

```
9131
```

**Wyjście:**

```
4951
```

### Uwagi

* Jeśli liczba ma nieparzystą liczbę bitów, najwyższy (samotny) bit pozostaje bez zmian.

*/

function odwrocSasiadujaceBity(liczba) {
  let binary = (liczba >>> 0).toString(2); // konwersja na system binarny
  let n = binary.length;
  let wynik = "";

  for (let i = 0; i < n; i += 2) {
    // zamiana sasiadujacych bitow
    if (i == n - 1) {
      // dodanie ostatniego bitu, jesli dlugosc binarna jest nieparzysta
      wynik += binary[i];
    } else {
      wynik += binary[i + 1] + binary[i];
    }
  }

  return parseInt(wynik, 2); // konwersja na system dziesietny
}

// test
function test() {
  let input = 9131;
  let expectedOutput = 4951;
  let output = odwrocSasiadujaceBity(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

