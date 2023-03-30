/*

Tytul: Sortowanie napisow w liscie wzgledem dlugosci.

Tresc: Masz dana liste napisow. Posortuj napisy w liscie wzgledem dlugosci.

Dane wejsciowe: Lista napisow.

Dane wyjsciowe: Lista napisow.

Przyklad:

Dla listy ["abcd", "ab", "a", "abc"] powinno zostac zwrocone ["a", "ab", "abc", "abcd"].

*/

const sortowanieNapisowDlugosc = (lista) => {
  return lista.sort((a, b) => a.length - b.length);
};

// Testy
const lista1 = ["abcd", "ab", "a", "abc"];
const wynik1 = ["a", "ab", "abc", "abcd"];
const lista2 = ["kot", "pies", "zaba", "krowa"];
const wynik2 = ["kot", "pies", "zaba", "krowa"];

console.assert(
  JSON.stringify(sortowanieNapisowDlugosc(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortowanieNapisowDlugosc(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);

