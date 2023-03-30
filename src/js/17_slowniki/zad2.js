/*

Tytuł: Słownik z kluczami będącymi elementami jednej listy i wartościami elementami drugiej listy.

Treść: Dostajesz dwie listy liczb całkowitych. Stwórz słownik, w którym kluczami będą elementy pierwszej listy, a wartościami elementy drugiej listy. Jeśli listy są różnej długości, zwróć pusty słownik.

Dane wejściowe: Dwie listy liczb całkowitych.

Dane wyjściowe: Słownik z kluczami i wartościami będącymi liczbami całkowitymi.

Przykład:

Dla otrzymanych list: [3, 5, 8] i [1, 2, -1], słownik powinien wyglądać następująco: {3: 1, 5: 2, 8: -1}.

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
  console.assert(slownik1[3] === 1, "Test 1 nie powiódł się");
  console.assert(slownik1[5] === 2, "Test 2 nie powiódł się");
  console.assert(slownik1[8] === -1, "Test 3 nie powiódł się");

  const slownik2 = stworzSlownik([1, 2, 3, 4], [10, 20, 30]);
  console.assert(Object.keys(slownik2).length === 0, "Test 4 nie powiódł się");

  const slownik3 = stworzSlownik([], []);
  console.assert(Object.keys(slownik3).length === 0, "Test 5 nie powiódł się");
}

testSlownik();
