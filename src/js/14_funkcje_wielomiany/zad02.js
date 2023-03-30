/*

Tytul: Obliczenie iloczynu wielomianu przez skalar.

Tresc: Otrzymujesz liste n wspolczynnikow wielomianu w postaci $a_nx^n + a_{n-1}x^{n-1} + ... + a_0$ oraz liczbe x. Oblicz wspolczynniki wielomianu, ktory jest wynikiem pomnozenia otrzymanego wielomianu przez liczbe x.

Dane wejsciowe: Lista liczb naturalnych i liczba naturalna.

Dane wyjsciowe: Lista liczb naturalnych.

Przyklad:

Dla listy wspolczynnikow [4, -3, 2] i liczby x = -2, zostanie zwrocona lista [-8, 6, -4].
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

