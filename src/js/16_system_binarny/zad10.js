/*
ZAD-10 — Ile bitów trzeba odwrócić (A → B)

**Poziom:** ★★☆
**Tagi:** `XOR`, `popcount`, `bitwise`

### Treść

Wczytaj dwie liczby naturalne `A` i `B`. Oblicz, ile bitów trzeba odwrócić w `A`, aby otrzymać `B`.

### Wejście

* 1. linia: `A`
* 2. linia: `B`

### Wyjście

Jedna liczba naturalna: liczba różniących się bitów.

### Przykład

**Wejście:**

```
34
73
```

**Wyjście:**

```
5
```

*/

function zamien(a, b) {
  let wynik = 0;
  let xor = a ^ b;
  while (xor != 0) {
    wynik += xor & 1;
    xor >>= 1;
  }
  return wynik;
}

function test() {
  console.assert(zamien(34, 73) === 5, "Test 1 nie powiodl sie");
  console.assert(zamien(1, 1) === 0, "Test 2 nie powiodl sie");
  console.assert(zamien(0, 0) === 0, "Test 3 nie powiodl sie");
  console.assert(zamien(0, 1) === 1, "Test 4 nie powiodl sie");
  console.assert(zamien(1, 0) === 1, "Test 5 nie powiodl sie");
}

test();

