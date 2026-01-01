/*
ZAD-14 — Napis z liczb od 1 do n

**Poziom:** ★☆☆
**Tagi:** `pętle`, `string`

### Treść

Wczytaj `n` i wypisz napis złożony z kolejnych liczb od 1 do `n`, bez separatorów.

### Wejście

* 1. linia: liczba naturalna `n` (n ≥ 1)

### Wyjście

* 1. linia: ciąg `1..n` bez spacji

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
123
```

*/

// Funkcja tworzy napis z kolejnych liczb od 1 do n
// Złożoność czasowa: O(n), gdzie n to podana liczba
// Złożoność pamięciowa: O(n) dla przechowania wyniku
function napisOd1DoN(n) {
  let wynik = "";
  for (let i = 1; i <= n; i++) {
    wynik += i;
  }
  return wynik;
}

// Test

function test() {
  let input = 3;
  let expectedOutput = "123";
  let output = napisOd1DoN(input);

  console.assert(
    output === expectedOutput,
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

