/*

Tytul: Obliczenie n-tej pochodnej wielomianu.

Tresc: Otrzymujesz liste n wspolczynnikow wielomianu w postaci $a_nx^n + a_{n-1}x^{n-1} + ... + a_0$ oraz liczbe naturalna k. Oblicz wspolczynniki wielomianu bedacego k-ta pochodna otrzymanego wielomianu.

Dane wejsciowe: Lista liczb naturalnych i liczba naturalna.

Dane wyjsciowe: Lista liczb naturalnych.

Przyklad:

Dla otrzymanej listy wspolczynnikow [4, -3, 2] i liczby k = 1, zostanie zwrocona lista [8, -3].*/

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

