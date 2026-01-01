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

function wielomian(wspolczynniki, x) {
  let suma = 0;
  for (let i = 0; i < wspolczynniki.length; i++) {
    suma += wspolczynniki[i] * Math.pow(x, i);
  }
  return suma;
}

function test_wielomian() {
  console.assert(wielomian([3, 2, 1], 1) === 6, "Blad testu 1");
  console.assert(wielomian([3, 2, 1], 2) === 17, "Blad testu 2");
  console.assert(wielomian([3, 2, 1], 3) === 36, "Blad testu 3");
  console.assert(wielomian([3, 2, 1], 4) === 63, "Blad testu 4");
  console.assert(wielomian([3, 2, 1], 5) === 98, "Blad testu 5");
  console.assert(wielomian([3, 2, 1], 6) === 141, "Blad testu 6");
  console.assert(wielomian([3, 2, 1], 7) === 192, "Blad testu 7");
  console.assert(wielomian([3, 2, 1], 8) === 251, "Blad testu 8");
  console.assert(wielomian([3, 2, 1], 9) === 318, "Blad testu 9");
  console.assert(wielomian([3, 2, 1], 10) === 393, "Blad testu 10");
}

test_wielomian();

