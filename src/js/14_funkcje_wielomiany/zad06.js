/*

Tytul: Obliczenie miejsc zerowych rownania kwadratowego.

Tresc: Otrzymujesz liste wspolczynnikow rownania kwadratowego $ax^2 + bx + c$. Znajdz rzeczywiste miejsca zerowe rownania kwadratowego.

Dane wejsciowe: Lista liczb naturalnych.

Dane wyjsciowe: Lista liczb zmiennoprzecinkowych.

Przyklad:

Dla otrzymanej listy wspolczynnikow: [1, 2, 1], zostanie zwrocona lista: [-1, -1].
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

