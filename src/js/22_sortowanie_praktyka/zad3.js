/*

Tytul: Sortowanie listy par wzgledem jednej z kategorii.

Tresc: Masz dana liste par napisow i liczb. Posortuj pary w liscie wzgledem:

a) Liczb.
b) Dlugosci napisow.

Dane wejsciowe: Lista par napisow i liczb.

Dane wyjsciowe: Lista par napisow i liczb.

Przyklad:

Dla listy [(“ab”, 3), (“bca”, 1), (“c”, 2)] powinno zostac zwrocone:

a) [(“bca”, 1), (“c”, 2), (“ab”, 3)] lub
b) [(“c”, 2), (“ab”, 3), (“bca”, 1)].

*/

const sortowanieParLiczb = (lista) => {
  return lista.sort((a, b) => a[1] - b[1]);
};

const sortowanieParDlugosciNapisow = (lista) => {
  return lista.sort((a, b) => a[0].length - b[0].length);
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

console.assert(
  JSON.stringify(sortowanieParLiczb(lista)) === JSON.stringify(wynikA),
  "Test a nieudany"
);
console.assert(
  JSON.stringify(sortowanieParDlugosciNapisow(lista)) ===
    JSON.stringify(wynikB),
  "Test b nieudany"
);

