/*
Tytuł: Słownik z kluczami będącymi liczbami naturalnymi i wartościami ich kwadratami.

Treść: Dostajesz liczbę naturalną. Stwórz słownik, w którym kluczami będą kolejne liczby naturalne mniejsze od otrzymanej liczby, a wartościami będą ich kwadraty.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Słownik z kluczami i wartościami będącymi liczbami naturalnymi.

Przykład:

Dla liczby 5, słownik powinien wyglądać następująco: {1: 1, 2: 4, 3: 9, 4: 16}.
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
  assert(slownik1[1] === 1, "Test 1 nie powiódł się");
  assert(slownik1[2] === 4, "Test 2 nie powiódł się");
  assert(slownik1[3] === 9, "Test 3 nie powiódł się");
  assert(slownik1[4] === 16, "Test 4 nie powiódł się");

  const slownik2 = stworzSlownikKwadratow(10);
  assert(slownik2[6] === 36, "Test 5 nie powiódł się");
  assert(slownik2[9] === 81, "Test 6 nie powiódł się");
}

// test
function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Asercja nie powiodła się");
  }
}

testSlownikKwadratow();
