/*

Tytuł: Sortowanie listy liczb z zakresu 0-2.

Treść: Otrzymujesz listę liczb składających się tylko z zer, jedynek i dwójek. Posortuj tę listę.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Posortowana lista liczb naturalnych.

Przykład:
Dla listy: [1, 0, 1, 2, 2, 0, 1], powinna zostać zwrócona lista: [0, 0, 1, 1, 1, 2, 2].

*/

const sortuj = (lista) => {
  return lista.sort((a, b) => a - b);
};

const assert = (condition, message) => {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
};

// Testy
const lista1 = [1, 0, 1, 2, 2, 0, 1];
const wynik1 = [0, 0, 1, 1, 1, 2, 2];
const lista2 = [2, 0, 0, 1, 1, 2, 0];
const wynik2 = [0, 0, 0, 1, 1, 2, 2];

assert(
  JSON.stringify(sortuj(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
assert(
  JSON.stringify(sortuj(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
