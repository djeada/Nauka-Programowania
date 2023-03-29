/*

Tytuł: Sortowanie listy par względem jednej z kategorii.

Treść: Masz daną listę par napisów i liczb. Posortuj pary w liście względem:

a) Liczb.
b) Długości napisów.

Dane wejściowe: Lista par napisów i liczb.

Dane wyjściowe: Lista par napisów i liczb.

Przykład:

Dla listy [(“ab”, 3), (“bca”, 1), (“c”, 2)] powinno zostać zwrócone:

a) [(“bca”, 1), (“c”, 2), (“ab”, 3)] lub
b) [(“c”, 2), (“ab”, 3), (“bca”, 1)].

*/

const sortowanieParLiczb = (lista) => {
  return lista.sort((a, b) => a[1] - b[1]);
};

const sortowanieParDlugosciNapisow = (lista) => {
  return lista.sort((a, b) => a[0].length - b[0].length);
};

const assert = (condition, message) => {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
};

// Testy
const lista = [
  ["ab", 3],
  ["bca", 1],
  ["c", 2],
];
const wynikA = [
  ["bca", 1],
  ["c", 2],
  ["ab", 3],
];
const wynikB = [
  ["c", 2],
  ["ab", 3],
  ["bca", 1],
];

assert(
  JSON.stringify(sortowanieParLiczb(lista)) === JSON.stringify(wynikA),
  "Test a nieudany"
);
assert(
  JSON.stringify(sortowanieParDlugosciNapisow(lista)) ===
    JSON.stringify(wynikB),
  "Test b nieudany"
);
