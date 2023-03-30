/*

Tytul: Sortowanie listy binarnej.

Tresc: Otrzymujesz liste liczb skladajacych sie tylko z zer i jedynek. Posortuj te liste.

Dane wejsciowe: Lista liczb naturalnych.

Dane wyjsciowe: Posortowana lista liczb naturalnych.

Przyklad:
Dla listy: [1, 0, 1, 0, 1, 1], powinna zostac zwrocona lista: [0, 0, 1, 1, 1, 1].

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

