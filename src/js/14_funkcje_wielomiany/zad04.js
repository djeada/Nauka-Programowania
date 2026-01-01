/*
ZAD-04 — Mnożenie wielomianów

**Poziom:** ★★☆
**Tagi:** `funkcje`, `wielomiany`, `konwolucja`

### Treść

Napisz funkcję, która otrzymuje dwie listy współczynników wielomianów `a` i `b` i zwraca listę współczynników wielomianu będącego ich iloczynem.

### Wejście (argumenty funkcji)

* `a` — lista `[a_n, ..., a_0]`
* `b` — lista `[b_m, ..., b_0]`

### Wyjście (zwracana wartość)

* lista współczynników wielomianu `a * b` (długość `len(a)+len(b)-1`)

### Przykład

Dla `a = [5, 0, 10, 6]` oraz `b = [1, 2, 4]` funkcja zwraca:
`[5, 10, 30, 26, 52, 24]`

*/

function mnozenieWielomianow(wielomian1, wielomian2) {
  const wynik = new Array(wielomian1.length + wielomian2.length - 1).fill(0);

  for (let i = 0; i < wielomian1.length; i++) {
    for (let j = 0; j < wielomian2.length; j++) {
      wynik[i + j] += wielomian1[i] * wielomian2[j];
    }
  }

  return wynik;
}

// Testy
function testMnozenieWielomianow() {
  let wielomian1;
  let wielomian2;
  let wynik;

  wielomian1 = [5, 0, 10, 6];
  wielomian2 = [1, 2, 4];
  wynik = mnozenieWielomianow(wielomian1, wielomian2);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([5, 10, 30, 26, 52, 24]),
    "Test 1 nieudany"
  );

  wielomian1 = [1, 2];
  wielomian2 = [2, 1];
  wynik = mnozenieWielomianow(wielomian1, wielomian2);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([2, 5, 2]),
    "Test 2 nieudany"
  );

  wielomian1 = [1, 1];
  wielomian2 = [1, 1];
  wynik = mnozenieWielomianow(wielomian1, wielomian2);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([1, 2, 1]),
    "Test 3 nieudany"
  );
}

testMnozenieWielomianow();
console.log("Wszystkie testy zakonczone sukcesem");

