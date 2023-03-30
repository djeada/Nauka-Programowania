/*

Tytul: Sortowanie wzgledem kluczy/wartosci

Otrzymujesz slownik skladajacy sie z par napisow i liczb calkowitych. Twoim zadaniem jest wypisanie par posortowanych wzgledem napisow oraz wzgledem liczb.

Dane wejsciowe: Slownik par: napis, liczba calkowita.

Dane wyjsciowe: Lista par.

Przyklad:

Dla otrzymanego slownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostac zwrocony slownik: [("a", -2), ("b", 4), ("c", 3), ("x", 5)].
Dla otrzymanego slownika: {"c": 3, "x": 5, "a": -2, "b": 4}, powinien zostac zwrocony slownik: [("a", -2), ("c", 3), ("b", 4), ("x", 5)].


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
  console.assert(wynik.length === poprawnyWynik.length, "Test nie powiodl sie");
  for (let i = 0; i < wynik.length; i++) {
    console.assert(wynik[i][0] === poprawnyWynik[i][0], "Test nie powiodl sie");
    console.assert(wynik[i][1] === poprawnyWynik[i][1], "Test nie powiodl sie");
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
  console.assert(wynik.length === poprawnyWynik.length, "Test nie powiodl sie");
  for (let i = 0; i < wynik.length; i++) {
    console.assert(wynik[i][0] === poprawnyWynik[i][0], "Test nie powiodl sie");
    console.assert(wynik[i][1] === poprawnyWynik[i][1], "Test nie powiodl sie");
  }
}

testSortujSlownikPoKluczach();
testSortujSlownikPoWartosciach();

