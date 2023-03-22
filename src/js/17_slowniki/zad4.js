/*

Tytuł: Usuwanie z słownika.

Treść: Otrzymujesz słownik par napisów i liczb całkowitych oraz pojedynczą liczbę całkowitą. Usuń z słownika pary, dla których wartość jest równa otrzymanej liczbie.

Dane wejściowe: Słownik par napisów i liczb całkowitych oraz liczba całkowita.

Dane wyjściowe: Słownik par napisów i liczb całkowitych.

Przykład:

Dla słownika i liczby: {“aaa”: 5, “abc”: 1, “xxx”: 5, “cba” : 3} i 5, słownik powinien wyglądać następująco: {“abc”: 1, “cba” : 3}.

*/

function usunZeSlownika(slownik, liczba) {
  for (let key in slownik) {
    if (slownik[key] === liczba) {
      delete slownik[key];
    }
  }
  return slownik;
}

function testUsunZeSlownika() {
  const slownik1 = { aaa: 5, abc: 1, xxx: 5, cba: 3 };
  const wynik1 = usunZeSlownika(slownik1, 5);
  assert(wynik1["abc"] === 1, "Test 1 nie powiódł się");
  assert(wynik1["cba"] === 3, "Test 2 nie powiódł się");
  assert(Object.keys(wynik1).length === 2, "Test 3 nie powiódł się");

  const slownik2 = { a: 10, b: 20, c: 30 };
  const wynik2 = usunZeSlownika(slownik2, 15);
  assert(Object.keys(wynik2).length === 3, "Test 4 nie powiódł się");
}

// test
function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Asercja nie powiodła się");
  }
}

testUsunZeSlownika();
