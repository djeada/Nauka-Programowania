/*
ZAD-05 — k-ta pochodna wielomianu

**Poziom:** ★★☆
**Tagi:** `funkcje`, `pochodna`, `wielomiany`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę naturalną `k` i zwraca współczynniki wielomianu będącego **k-tą pochodną**.

### Wejście (argumenty funkcji)

* `a` — lista `[a_n, ..., a_0]`
* `k` — liczba naturalna

### Wyjście (zwracana wartość)

* lista współczynników wielomianu po zróżniczkowaniu `k` razy

### Przykład

Dla `a = [4, -3, 2]` oraz `k = 1` funkcja zwraca:
`[8, -3]`

### Uwagi

* Jeśli `k` jest większe niż stopień wielomianu, wynikiem jest wielomian zerowy: `[0]`.

*/

function pochodnaWielomianu(wspolczynniki, k) {
  for (let i = 0; i < k; i++) {
    for (let j = wspolczynniki.length - 1; j > 0; j--) {
      wspolczynniki[j - 1] = wspolczynniki[j] * j;
    }
    wspolczynniki.pop();
  }
  return wspolczynniki;
}

// Testy
function testPochodnaWielomianu() {
  let wspolczynniki;
  let k;
  let wynik;

  wspolczynniki = [4, -3, 2];
  k = 1;
  wynik = pochodnaWielomianu(wspolczynniki, k);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([8, -3]),
    "Test 1 nieudany"
  );

  wspolczynniki = [6, -5, 4, -3];
  k = 2;
  wynik = pochodnaWielomianu(wspolczynniki, k);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([36, -20, 4]),
    "Test 2 nieudany"
  );

  wspolczynniki = [1, 2, 3, 4];
  k = 3;
  wynik = pochodnaWielomianu(wspolczynniki, k);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([24]),
    "Test 3 nieudany"
  );
}

testPochodnaWielomianu();
console.log("Wszystkie testy zakonczone sukcesem");

