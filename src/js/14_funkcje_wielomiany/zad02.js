/*
ZAD-02 — Iloczyn wielomianu przez skalar

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `wielomiany`, `skalar`

### Treść

Napisz funkcję, która otrzymuje listę współczynników wielomianu `a` oraz liczbę `k`, a następnie zwraca współczynniki wielomianu powstałego z pomnożenia każdego współczynnika przez `k`.

### Wejście (argumenty funkcji)

* `a` — lista współczynników `[a_n, ..., a_0]`
* `k` — liczba (całkowita)

### Wyjście (zwracana wartość)

* lista współczynników wielomianu `k * P(x)`

### Przykład

Dla `a = [4, -3, 2]` i `k = -2` funkcja zwraca:
`[-8, 6, -4]`

*/
function mnozenieWielomianuPrzezSkalar(wspolczynniki, skalar) {
  return wspolczynniki.map((wspolczynnik) => wspolczynnik * skalar);
}

// Testy
function testMnozenieWielomianuPrzezSkalar() {
  let wielomian;
  let skalar;
  let wynik;

  wielomian = [4, -3, 2];
  skalar = -2;
  wynik = mnozenieWielomianuPrzezSkalar(wielomian, skalar);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([-8, 6, -4]),
    "Test 1 nieudany"
  );

  wielomian = [5, 0, -1];
  skalar = 3;
  wynik = mnozenieWielomianuPrzezSkalar(wielomian, skalar);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([15, 0, -3]),
    "Test 2 nieudany"
  );

  wielomian = [0, 0, 0];
  skalar = 5;
  wynik = mnozenieWielomianuPrzezSkalar(wielomian, skalar);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([0, 0, 0]),
    "Test 3 nieudany"
  );
}

testMnozenieWielomianuPrzezSkalar();
console.log("Wszystkie testy zakonczone sukcesem");

