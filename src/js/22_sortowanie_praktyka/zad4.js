/*

Tytuł: Sortowanie napisów w liście względem długości.

Treść: Masz daną listę napisów. Posortuj napisy w liście względem długości.

Dane wejściowe: Lista napisów.

Dane wyjściowe: Lista napisów.

Przykład:

Dla listy ["abcd", "ab", "a", "abc"] powinno zostać zwrócone ["a", "ab", "abc", "abcd"].

*/

const sortowanieNapisowDlugosc = (lista) => {
  return lista.sort((a, b) => a.length - b.length);
};

const assert = (condition, message) => {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
};

// Testy
const lista1 = ["abcd", "ab", "a", "abc"];
const wynik1 = ["a", "ab", "abc", "abcd"];
const lista2 = ["kot", "pies", "żaba", "krowa"];
const wynik2 = ["kot", "pies", "żaba", "krowa"];

assert(
  JSON.stringify(sortowanieNapisowDlugosc(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
assert(
  JSON.stringify(sortowanieNapisowDlugosc(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
