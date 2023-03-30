/*

Tytuł: Sortowanie względem kluczy/wartości

Otrzymujesz słownik składający się z par napisów i liczb całkowitych. Twoim zadaniem jest wypisanie par posortowanych względem napisów oraz względem liczb.

Dane wejściowe: Słownik par: napis, liczba całkowita.

Dane wyjściowe: Lista par.

Przykład:

Dla otrzymanego słownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostać zwrócony słownik: [("a", -2), ("b", 4), ("c", 3), ("x", 5)].
Dla otrzymanego słownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostać zwrócony słownik: [("a", -2), ("c", 3), ("b", 4), ("x", 5)].


*/

function sortujSlownikPoKluczach(slownik) {
  const posortowaneKlucze = Object.keys(slownik).sort();
  const wynik = posortowaneKlucze.map((klucz) => [klucz, slownik[klucz]]);
  return wynik;
}

function sortujSlownikPoWartosciach(slownik) {
  const posortowaneKlucze = Object.keys(slownik).sort(
    (a, b) => slownik[a] - slownik[b]
  );
  const wynik = posortowaneKlucze.map((klucz) => [klucz, slownik[klucz]]);
  return wynik;
}

function testSortujSlownikPoKluczach() {
  const slownik = {
    c: 3,
    x: 5,
    a: -2,
    b: 4,
  };
  const wynik = sortujSlownikPoKluczach(slownik);
  const poprawnyWynik = [
    ["a", -2],
    ["b", 4],
    ["c", 3],
    ["x", 5],
  ];
  console.assert(wynik.length === poprawnyWynik.length, "Test nie powiódł się");
  for (let i = 0; i < wynik.length; i++) {
    console.assert(wynik[i][0] === poprawnyWynik[i][0], "Test nie powiódł się");
    console.assert(wynik[i][1] === poprawnyWynik[i][1], "Test nie powiódł się");
  }
}

function testSortujSlownikPoWartosciach() {
  const slownik = {
    c: 3,
    x: 5,
    a: -2,
    b: 4,
  };
  const wynik = sortujSlownikPoWartosciach(slownik);
  const poprawnyWynik = [
    ["a", -2],
    ["c", 3],
    ["b", 4],
    ["x", 5],
  ];
  console.assert(wynik.length === poprawnyWynik.length, "Test nie powiódł się");
  for (let i = 0; i < wynik.length; i++) {
    console.assert(wynik[i][0] === poprawnyWynik[i][0], "Test nie powiódł się");
    console.assert(wynik[i][1] === poprawnyWynik[i][1], "Test nie powiódł się");
  }
}

testSortujSlownikPoKluczach();
testSortujSlownikPoWartosciach();
