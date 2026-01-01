/*
ZAD-13 — Znaki na indeksach będących liczbami pierwszymi

**Poziom:** ★☆☆
**Tagi:** `liczby pierwsze`, `indeksy`, `string`

### Treść

Wczytaj napis. Zbierz znaki, których **indeksy (od 0)** są liczbami pierwszymi (2, 3, 5, 7, ...). Wypisz wynik jako listę w stylu Pythona.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: lista znaków, np. `['o', 'ń']`

### Przykład

**Wejście:**

```
Słoń
```

**Wyjście:**

```
['o', 'ń']
```

### Uwagi

* Indeksy: `S(0) ł(1) o(2) ń(3)` → bierz 2 i 3.

*/

// Funkcja sprawdza czy liczba jest pierwsza
// Złożoność czasowa: O(√n), gdzie n to wartość liczby
// Złożoność pamięciowa: O(1)
function czyLiczbaPierwsza(n) {
  if (n < 2) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}

// Funkcja zwraca znaki znajdujące się na pozycjach będących liczbami pierwszymi
// Złożoność czasowa: O(n√n), gdzie n to długość napisu
// Złożoność pamięciowa: O(k), gdzie k to liczba znalezionych znaków
function znakiNaPozycjachPierwszych(napis) {
  let wynik = [];
  for (let i = 0; i < napis.length; i++) {
    if (czyLiczbaPierwsza(i)) {
      wynik.push(napis[i]);
    }
  }
  return wynik;
}

// Test

function test() {
  let input = "Slon";
  let expectedOutput = ["o", "n"];
  let output = znakiNaPozycjachPierwszych(input);

  console.assert(
    JSON.stringify(output) === JSON.stringify(expectedOutput),
    "Test nie powiodl sie dla " +
      input +
      ". Otrzymany wynik to " +
      output +
      ", a oczekiwany wynik to " +
      expectedOutput
  );
  console.log("Test przeszedl pomyslnie");
}

test();

