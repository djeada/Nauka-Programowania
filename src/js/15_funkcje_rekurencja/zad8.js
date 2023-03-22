/*

Tytuł: Wieża Hanoi.

Treść: N krążków o różnych średnicach ułożonych jest na jednym z trzech słupków (A, B lub C). Na dole znajduje się krążek o największej średnicy. Każdy następny jest mniejszy od poprzedniego. Znajdź sposób na przełożenie wszystkich krążków na inny słupek. Pamiętaj, że nie wolno kłaść krążka o większej średnicy na krążek o mniejszej średnicy, ani przekładać kilku krążków jednocześnie.

Dane wejściowe: Liczba naturalna N.

Dane wyjściowe: Lista par znaków.

Przykład:

Dla N = 3, powinna zostać zwrócona lista: [('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'B'), ('C', 'A'), ('C', 'B'), ('A', 'B')]
*/

function wiezaHanoi(n, zrodlo = "A", cel = "B", pomocniczy = "C") {
  if (n === 1) {
    return [[zrodlo, cel]];
  } else {
    const ruchy1 = wiezaHanoi(n - 1, zrodlo, pomocniczy, cel);
    const ruchy2 = wiezaHanoi(1, zrodlo, cel, pomocniczy);
    const ruchy3 = wiezaHanoi(n - 1, pomocniczy, cel, zrodlo);
    return ruchy1.concat(ruchy2, ruchy3);
  }
}

function assert(warunek, komunikat) {
  if (!warunek) {
    throw komunikat || "Wystąpił błąd";
  }
}

// Testy
function testWiezaHanoi() {
  let n;
  let wynik;

  n = 1;
  wynik = wiezaHanoi(n);
  assert(
    JSON.stringify(wynik) === JSON.stringify([["A", "B"]]),
    "Test 1 nieudany"
  );

  n = 2;
  wynik = wiezaHanoi(n);
  assert(
    JSON.stringify(wynik) ===
      JSON.stringify([
        ["A", "C"],
        ["A", "B"],
        ["C", "B"],
      ]),
    "Test 2 nieudany"
  );

  n = 3;
  wynik = wiezaHanoi(n);
  assert(
    JSON.stringify(wynik) ===
      JSON.stringify([
        ["A", "B"],
        ["A", "C"],
        ["B", "C"],
        ["A", "B"],
        ["C", "A"],
        ["C", "B"],
        ["A", "B"],
      ]),
    "Test 3 nieudany"
  );
}

testWiezaHanoi();
console.log("Wszystkie testy zakończone sukcesem");
