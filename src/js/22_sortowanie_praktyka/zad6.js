/*

Tytuł: Sortowanie listy binarnej.

Treść: Otrzymujesz listę liczb składających się tylko z zer i jedynek. Posortuj tę listę.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Posortowana lista liczb naturalnych.

Przykład:
Dla listy: [1, 0, 1, 0, 1, 1], powinna zostać zwrócona lista: [0, 0, 1, 1, 1, 1].

*/

const sortowanieListyBinarnej = (lista) => {
  return lista.sort((a, b) => a - b);
};

// Testy
const lista1 = [1, 0, 1, 0, 1, 1];
const wynik1 = [0, 0, 1, 1, 1, 1];
const lista2 = [1, 1, 0, 0, 1, 0];
const wynik2 = [0, 0, 0, 1, 1, 1];

console.assert(
  JSON.stringify(sortowanieListyBinarnej(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortowanieListyBinarnej(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
