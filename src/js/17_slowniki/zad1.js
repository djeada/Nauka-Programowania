/*
Tytul: Slownik z kluczami bedacymi liczbami naturalnymi i wartosciami ich kwadratami.

Tresc: Dostajesz liczbe naturalna. Stworz slownik, w ktorym kluczami beda kolejne liczby naturalne mniejsze od otrzymanej liczby, a wartosciami beda ich kwadraty.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Slownik z kluczami i wartosciami bedacymi liczbami naturalnymi.

Przyklad:

Dla liczby 5, slownik powinien wygladac nastepujaco: {1: 1, 2: 4, 3: 9, 4: 16}.
*/

function stworzSlownikKwadratow(n) {
  const slownik = {};
  for (let i = 1; i < n; i++) {
    slownik[i] = i * i;
  }
  return slownik;
}

function testSlownikKwadratow() {
  const slownik1 = stworzSlownikKwadratow(5);
  console.assert(slownik1[1] === 1, "Test 1 nie powiodl sie");
  console.assert(slownik1[2] === 4, "Test 2 nie powiodl sie");
  console.assert(slownik1[3] === 9, "Test 3 nie powiodl sie");
  console.assert(slownik1[4] === 16, "Test 4 nie powiodl sie");

  const slownik2 = stworzSlownikKwadratow(10);
  console.assert(slownik2[6] === 36, "Test 5 nie powiodl sie");
  console.assert(slownik2[9] === 81, "Test 6 nie powiodl sie");
}

testSlownikKwadratow();

