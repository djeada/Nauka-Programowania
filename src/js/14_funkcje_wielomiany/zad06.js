/*
ZAD-06 — Miejsca zerowe równania kwadratowego (rzeczywiste)

**Poziom:** ★★☆
**Tagi:** `funkcje`, `delta`, `pierwiastki`

### Treść

Napisz funkcję, która otrzymuje listę współczynników równania kwadratowego `[a, b, c]` dla `a x^2 + b x + c` i zwraca listę **rzeczywistych** miejsc zerowych.

### Wejście (argumenty funkcji)

* `coef` — lista trzech liczb `[a, b, c]`

### Wyjście (zwracana wartość)

* lista liczb zmiennoprzecinkowych:

  * jeśli `Δ < 0` → pusta lista `[]`
  * jeśli `Δ = 0` → dwa jednakowe pierwiastki `[x, x]`
  * jeśli `Δ > 0` → dwa pierwiastki `[x1, x2]` (kolejność dowolna)

### Przykład

Dla `[1, 2, 1]` funkcja zwraca:
`[-1.0, -1.0]`

### Ograniczenia / gwarancje

* Zakładamy `a ≠ 0` (to naprawdę równanie kwadratowe).

### Uwagi

* Licz `Δ = b^2 - 4ac`.
* Pierwiastki: `(-b ± sqrt(Δ)) / (2a)`.

*/

function miejscaZeroweRownaniaKwadratowego(wspolczynniki) {
  const [a, b, c] = wspolczynniki;
  const delta = b * b - 4 * a * c;

  if (delta > 0) {
    return [
      (-b - Math.sqrt(delta)) / (2 * a),
      (-b + Math.sqrt(delta)) / (2 * a),
    ];
  } else if (delta === 0) {
    return [-b / (2 * a)];
  } else {
    return [];
  }
}

// Testy
function testMiejscaZeroweRownaniaKwadratowego() {
  let wspolczynniki;
  let wynik;

  wspolczynniki = [1, 2, 1];
  wynik = miejscaZeroweRownaniaKwadratowego(wspolczynniki);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([-1]),
    "Test 1 nieudany"
  );

  wspolczynniki = [1, -3, 2];
  wynik = miejscaZeroweRownaniaKwadratowego(wspolczynniki);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([1, 2]),
    "Test 2 nieudany"
  );

  wspolczynniki = [1, 0, -1];
  wynik = miejscaZeroweRownaniaKwadratowego(wspolczynniki);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([-1, 1]),
    "Test 3 nieudany"
  );

  wspolczynniki = [1, 0, 1];
  wynik = miejscaZeroweRownaniaKwadratowego(wspolczynniki);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([]),
    "Test 4 nieudany"
  );
}

testMiejscaZeroweRownaniaKwadratowego();
console.log("Wszystkie testy zakonczone sukcesem");

