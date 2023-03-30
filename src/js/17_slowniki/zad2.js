/*

Tytul: Slownik z kluczami bedacymi elementami jednej listy i wartosciami elementami drugiej listy.

Tresc: Dostajesz dwie listy liczb calkowitych. Stworz slownik, w ktorym kluczami beda elementy pierwszej listy, a wartosciami elementy drugiej listy. Jesli listy sa roznej dlugosci, zwroc pusty slownik.

Dane wejsciowe: Dwie listy liczb calkowitych.

Dane wyjsciowe: Slownik z kluczami i wartosciami bedacymi liczbami calkowitymi.

Przyklad:

Dla otrzymanych list: [3, 5, 8] i [1, 2, -1], slownik powinien wygladac nastepujaco: {3: 1, 5: 2, 8: -1}.

*/

function stworzSlownik(list1, list2) {
  const slownik = {};
  const dlugosc1 = list1.length;
  const dlugosc2 = list2.length;
  if (dlugosc1 !== dlugosc2) {
    return slownik;
  }
  for (let i = 0; i < dlugosc1; i++) {
    slownik[list1[i]] = list2[i];
  }
  return slownik;
}

function testSlownik() {
  const slownik1 = stworzSlownik([3, 5, 8], [1, 2, -1]);
  console.assert(slownik1[3] === 1, "Test 1 nie powiodl sie");
  console.assert(slownik1[5] === 2, "Test 2 nie powiodl sie");
  console.assert(slownik1[8] === -1, "Test 3 nie powiodl sie");

  const slownik2 = stworzSlownik([1, 2, 3, 4], [10, 20, 30]);
  console.assert(Object.keys(slownik2).length === 0, "Test 4 nie powiodl sie");

  const slownik3 = stworzSlownik([], []);
  console.assert(Object.keys(slownik3).length === 0, "Test 5 nie powiodl sie");
}

testSlownik();

