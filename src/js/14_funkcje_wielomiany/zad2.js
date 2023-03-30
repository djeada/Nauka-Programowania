/*

Tytuł: Obliczenie iloczynu wielomianu przez skalar.

Treść: Otrzymujesz listę n współczynników wielomianu w postaci $a_nx^n + a_{n-1}x^{n-1} + ... + a_0$ oraz liczbę x. Oblicz współczynniki wielomianu, który jest wynikiem pomnożenia otrzymanego wielomianu przez liczbę x.

Dane wejściowe: Lista liczb naturalnych i liczba naturalna.

Dane wyjściowe: Lista liczb naturalnych.

Przykład:

Dla listy współczynników [4, -3, 2] i liczby x = -2, zostanie zwrócona lista [-8, 6, -4].
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
console.log("Wszystkie testy zakończone sukcesem");
