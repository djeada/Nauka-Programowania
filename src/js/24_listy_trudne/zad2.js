/*

Tytuł: Przesuń zera.

Treść: Otrzymujesz listę liczb całkowitych. Przesuń wszystkie zera na koniec listy.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Lista liczb całkowitych.

Przykład:

Dla otrzymanej listy: [0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0], powinna zostać zwrócona lista: [1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0].

*/

const przesunZera = (lista) => {
  let zero = [];
  let result = [];
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] === 0) {
      zero.push(lista[i]);
    } else {
      result.push(lista[i]);
    }
  }
  return result.concat(zero);
};

const assert = (condition, message) => {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
};

// Testy
const lista1 = [0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0];
const wynik1 = [1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0];
const lista2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
const wynik2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

assert(
  JSON.stringify(przesunZera(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
assert(
  JSON.stringify(przesunZera(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
