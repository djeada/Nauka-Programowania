/*

Tytul: Sortowanie listy liczb z zakresu 0-2.

Tresc: Otrzymujesz liste liczb skladajacych sie tylko z zer, jedynek i dwojek. Posortuj te liste.

Dane wejsciowe: Lista liczb naturalnych.

Dane wyjsciowe: Posortowana lista liczb naturalnych.

Przyklad:
Dla listy: [1, 0, 1, 2, 2, 0, 1], powinna zostac zwrocona lista: [0, 0, 1, 1, 1, 2, 2].

*/

const sortuj = (lista) => {
  return lista.sort((a, b) => a - b);
};

// Testy
const lista1 = [1, 0, 1, 2, 2, 0, 1];
const wynik1 = [0, 0, 1, 1, 1, 2, 2];
const lista2 = [2, 0, 0, 1, 1, 2, 0];
const wynik2 = [0, 0, 0, 1, 1, 2, 2];

console.assert(
  JSON.stringify(sortuj(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortuj(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);

