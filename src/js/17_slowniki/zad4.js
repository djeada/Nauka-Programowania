/*

Tytul: Usuwanie z slownika.

Tresc: Otrzymujesz slownik par napisow i liczb calkowitych oraz pojedyncza liczbe calkowita. Usun z slownika pary, dla ktorych wartosc jest rowna otrzymanej liczbie.

Dane wejsciowe: Slownik par napisow i liczb calkowitych oraz liczba calkowita.

Dane wyjsciowe: Slownik par napisow i liczb calkowitych.

Przyklad:

Dla slownika i liczby: {“aaa”: 5, “abc”: 1, “xxx”: 5, “cba” : 3} i 5, slownik powinien wygladac nastepujaco: {“abc”: 1, “cba” : 3}.

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
  const slownik1 = {
    aaa: 5,
    abc: 1,
    xxx: 5,
    cba: 3,
  };
  const wynik1 = usunZeSlownika(slownik1, 5);
  console.assert(wynik1["abc"] === 1, "Test 1 nie powiodl sie");
  console.assert(wynik1["cba"] === 3, "Test 2 nie powiodl sie");
  console.assert(Object.keys(wynik1).length === 2, "Test 3 nie powiodl sie");

  const slownik2 = {
    a: 10,
    b: 20,
    c: 30,
  };
  const wynik2 = usunZeSlownika(slownik2, 15);
  console.assert(Object.keys(wynik2).length === 3, "Test 4 nie powiodl sie");
}

testUsunZeSlownika();

