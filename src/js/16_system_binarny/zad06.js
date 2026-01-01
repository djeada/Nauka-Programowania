/*
ZAD-06 — Konwersja między dowolnymi systemami (2..36)

**Poziom:** ★★☆
**Tagi:** `konwersja`, `base`, `string`

### Treść

Wczytaj:

1. liczbę `X` zapisaną w systemie o podstawie `p`
2. podstawę `p` (2..36)
3. podstawę docelową `q` (2..36)

i wypisz reprezentację `X` w systemie o podstawie `q`.

### Wejście

Trzy linie:

1. `X` (zapis liczby; dla podstaw >10 może zawierać litery `A-Z`)
2. `p` (2..36)
3. `q` (2..36)

### Wyjście

Jedna linia: zapis liczby w systemie o podstawie `q` (używaj `0–9` i `A–Z`).

### Przykład

**Wejście:**

```
4301
10
4
```

**Wyjście:**

```
1003031
```

### Uwagi o formacie

* `X` może być duże — traktuj jako napis, a nie typ int „na wejściu”.
* Dla wartości 10..35 stosuj `A..Z`.

*/
function konwersjaSystemow(liczba, podstawa1, podstawa2) {
  let dziesietna = 0;
  let reszta = 0;
  let potega = 0;
  let wynik = "";

  // konwersja na system dziesietny
  while (liczba > 0) {
    reszta = liczba % 10;
    dziesietna += reszta * Math.pow(podstawa1, potega);
    potega++;
    liczba = Math.floor(liczba / 10);
  }

  // konwersja na nowy system
  while (dziesietna > 0) {
    reszta = dziesietna % podstawa2;
    wynik = reszta + wynik;
    dziesietna = Math.floor(dziesietna / podstawa2);
  }

  return wynik ? wynik : "0";
}

// testy
function test() {
  const liczba1 = 4301;
  const podstawa1 = 10;
  const podstawa2 = 4;
  const wynik = "1003031";

  if (konwersjaSystemow(liczba1, podstawa1, podstawa2) === wynik) {
    console.log("Test zakonczony sukcesem.");
  } else {
    console.log("Test nie powiodl sie.");
  }
}

test();

