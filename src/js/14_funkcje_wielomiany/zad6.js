/*

Tytuł: Obliczenie miejsc zerowych równania kwadratowego.

Treść: Otrzymujesz listę współczynników równania kwadratowego $ax^2 + bx + c$. Znajdź rzeczywiste miejsca zerowe równania kwadratowego.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Lista liczb zmiennoprzecinkowych.

Przykład:

Dla otrzymanej listy współczynników: [1, 2, 1], zostanie zwrócona lista: [-1, -1].
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

function assert(warunek, komunikat) {
  if (!warunek) {
    throw komunikat || "Wystąpił błąd";
  }
}

// Testy
function testMiejscaZeroweRownaniaKwadratowego() {
  let wspolczynniki;
  let wynik;

  wspolczynniki = [1, 2, 1];
  wynik = miejscaZeroweRownaniaKwadratowego(wspolczynniki);
  assert(JSON.stringify(wynik) === JSON.stringify([-1]), "Test 1 nieudany");

  wspolczynniki = [1, -3, 2];
  wynik = miejscaZeroweRownaniaKwadratowego(wspolczynniki);
  assert(JSON.stringify(wynik) === JSON.stringify([1, 2]), "Test 2 nieudany");

  wspolczynniki = [1, 0, -1];
  wynik = miejscaZeroweRownaniaKwadratowego(wspolczynniki);
  assert(JSON.stringify(wynik) === JSON.stringify([-1, 1]), "Test 3 nieudany");

  wspolczynniki = [1, 0, 1];
  wynik = miejscaZeroweRownaniaKwadratowego(wspolczynniki);
  assert(JSON.stringify(wynik) === JSON.stringify([]), "Test 4 nieudany");
}

testMiejscaZeroweRownaniaKwadratowego();
console.log("Wszystkie testy zakończone sukcesem");
