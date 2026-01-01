/*
ZAD-01 — Wartość wielomianu w punkcie

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `Horner`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę `x`, a następnie zwraca wartość wielomianu w punkcie `x`.

### Wejście (argumenty funkcji)

* `a` — lista współczynników `[a_n, ..., a_0]`
* `x` — liczba naturalna (lub całkowita)

### Wyjście (zwracana wartość)

* jedna liczba (całkowita)

### Przykład

Dla `a = [3, 2, 1]` i `x = 1` funkcja zwraca:
`6`

### Uwagi

* Najprościej użyć schematu Hornera.

*/

// Funkcja oblicza wartość wielomianu w punkcie x
// Współczynniki podane od najwyższej potęgi do najniższej: [a_n, ..., a_0]
// Złożoność czasowa: O(n), gdzie n to stopień wielomianu
// Złożoność pamięciowa: O(1)
function wielomian(wspolczynniki, x) {
  let suma = 0;
  const n = wspolczynniki.length;
  for (let i = 0; i < n; i++) {
    // wspolczynniki[i] odpowiada potędze (n-1-i)
    suma += wspolczynniki[i] * Math.pow(x, n - 1 - i);
  }
  return suma;
}

function test_wielomian() {
  // [3, 2, 1] oznacza 3x^2 + 2x + 1
  console.assert(wielomian([3, 2, 1], 1) === 6, "Blad testu 1"); // 3 + 2 + 1 = 6
  console.assert(wielomian([3, 2, 1], 2) === 17, "Blad testu 2"); // 12 + 4 + 1 = 17
  console.assert(wielomian([3, 2, 1], 3) === 34, "Blad testu 3"); // 27 + 6 + 1 = 34
  console.assert(wielomian([3, 2, 1], 4) === 57, "Blad testu 4"); // 48 + 8 + 1 = 57
  console.assert(wielomian([3, 2, 1], 5) === 86, "Blad testu 5"); // 75 + 10 + 1 = 86
  console.assert(wielomian([1, 0, 0], 5) === 25, "Blad testu 6"); // 1*25 + 0 + 0 = 25
}

test_wielomian();
console.log("Wszystkie testy zakończone sukcesem");

