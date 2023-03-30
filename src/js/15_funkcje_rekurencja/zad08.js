/*

Tytul: Wieza Hanoi.

Tresc: N krazkow o roznych srednicach ulozonych jest na jednym z trzech slupkow (A, B lub C). Na dole znajduje sie krazek o najwiekszej srednicy. Kazdy nastepny jest mniejszy od poprzedniego. Znajdz sposob na przelozenie wszystkich krazkow na inny slupek. Pamietaj, ze nie wolno klasc krazka o wiekszej srednicy na krazek o mniejszej srednicy, ani przekladac kilku krazkow jednoczesnie.

Dane wejsciowe: Liczba naturalna N.

Dane wyjsciowe: Lista par znakow.

Przyklad:

Dla N = 3, powinna zostac zwrocona lista: [('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'B'), ('C', 'A'), ('C', 'B'), ('A', 'B')]
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

// Testy
function testWiezaHanoi() {
  let n;
  let wynik;

  n = 1;
  wynik = wiezaHanoi(n);
  console.assert(
    JSON.stringify(wynik) === JSON.stringify([["A", "B"]]),
    "Test 1 nieudany"
  );

  n = 2;
  wynik = wiezaHanoi(n);
  console.assert(
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
  console.assert(
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
console.log("Wszystkie testy zakonczone sukcesem");

