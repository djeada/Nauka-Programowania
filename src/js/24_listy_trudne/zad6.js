/*

Tytuł: Połączone posortowane listy 

Treść: Otrzymujesz listę zawierającą M posortowanych list. Połącz te listy w jedną posortowaną listę. Wszystkie elementy są unikalne.

Dane wejściowe: Lista list zawierających liczby naturalne.

Dane wyjściowe: Lista zawierająca liczby naturalne.

Przykład:

Dla wejściowej listy:
[[ -6, 23, 29, 33],
[ 6, 22, 35, 71 ],
[ 5, 19, 21, 37 ],
[ -12, -7, -3, 28 ]],

powinna zostać zwrócona lista: [-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71].

*/

const polaczListy = (lista) => {
  let result = [];
  for (let i = 0; i < lista.length; i++) {
    result = result.concat(lista[i]);
  }
  return result.sort((a, b) => a - b);
};

const assert = (condition, message) => {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
};

// Testy
const lista1 = [
  [-6, 23, 29, 33],
  [6, 22, 35, 71],
  [5, 19, 21, 37],
  [-12, -7, -3, 28],
];
const wynik1 = [-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71];
const lista2 = [
  [-6, 23, 29, 33],
  [6, 22, 35, 71],
  [5, 19, 21, 37],
  [-12, -7, -3, 28],
  [0, 1, 2, 3],
];
const wynik2 = [
  -12, -7, -6, -3, 0, 1, 2, 3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71,
];

assert(
  JSON.stringify(polaczListy(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
assert(
  JSON.stringify(polaczListy(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
