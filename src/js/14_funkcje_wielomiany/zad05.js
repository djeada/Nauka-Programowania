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
  // Tworzymy kopię tablicy aby nie modyfikować oryginału
  let wynik = [...wspolczynniki];
  
  for (let i = 0; i < k; i++) {
    if (wynik.length === 1) {
      return [0]; // Wielomian zerowy
    }
    
    const nowyWynik = [];
    for (let j = 0; j < wynik.length - 1; j++) {
      // Pochodna a_j * x^(n-j) to a_j * (n-j) * x^(n-j-1)
      nowyWynik.push(wynik[j] * (wynik.length - 1 - j));
    }
    wynik = nowyWynik;
  }
  
  return wynik.length === 0 ? [0] : wynik;
}

// Testy
function testPochodnaWielomianu() {
  let wspolczynniki;
  let k;
  let wynik;

  // Test 1: 4x^2 - 3x + 2, pochodna = 8x - 3
  wspolczynniki = [4, -3, 2];
  k = 1;
  wynik = pochodnaWielomianu(wspolczynniki, k);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([8, -3]),
    "Test 1 nieudany"
  );

  // Test 2: 6x^3 - 5x^2 + 4x - 3, druga pochodna = 36x - 10
  wspolczynniki = [6, -5, 4, -3];
  k = 2;
  wynik = pochodnaWielomianu(wspolczynniki, k);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([36, -10]),
    "Test 2 nieudany"
  );

  // Test 3: 1x^3 + 2x^2 + 3x + 4, trzecia pochodna = 6
  wspolczynniki = [1, 2, 3, 4];
  k = 3;
  wynik = pochodnaWielomianu(wspolczynniki, k);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([6]),
    "Test 3 nieudany"
  );
}

testPochodnaWielomianu();
console.log("Wszystkie testy zakonczone sukcesem");

