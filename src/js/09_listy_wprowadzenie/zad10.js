/*
Tytuł: Czy punkty mogą stanowić wierzchołki trójkąta?

Treść: Otrzymujesz dokładnie 6 liczb całkowitych, które odpowiadają współrzędnym punktów A, B, C w kolejności: xA, yA, xB, yB, xC, yC. Sprawdź, czy punkty A, B, C mogą stanowić wierzchołki trójkąta.

Dane wejściowe: Lista liczb całkowitych reprezentująca współrzędne punktów A, B, C.

Dane wyjściowe: Wartość logiczna określająca, czy punkty A, B, C mogą stanowić wierzchołki trójkąta.

Przykład:

Dla otrzymanej listy [-3, -2, -3, 1, -3, 0], powinna zostać zwrócona wartość logiczna: Fałsz.
*/

// Funkcja sprawdzająca, czy punkty mogą stanowić wierzchołki trójkąta
function czyTrojkat(punkty) {
  var xA = punkty[0];
  var yA = punkty[1];
  var xB = punkty[2];
  var yB = punkty[3];
  var xC = punkty[4];
  var yC = punkty[5];

  var AB = Math.sqrt(Math.pow(xB - xA, 2) + Math.pow(yB - yA, 2));
  var BC = Math.sqrt(Math.pow(xC - xB, 2) + Math.pow(yC - yB, 2));
  var AC = Math.sqrt(Math.pow(xC - xA, 2) + Math.pow(yC - yA, 2));

  return AB + BC > AC && AB + AC > BC && BC + AC > AB;
}

// Testy
function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
}

function testCzyTrojkat() {
  assert(czyTrojkat([-3, -2, -3, 1, -3, 0]) === false);
  assert(czyTrojkat([0, 0, 3, 0, 0, 4]) === true);
  assert(czyTrojkat([0, 0, 0, 0, 0, 0]) === false);
  assert(czyTrojkat([1, 2, 2, 2, 3, 2]) === false);
  assert(czyTrojkat([0, 0, 5, 0, 0, 5]) === true);
}

testCzyTrojkat();
