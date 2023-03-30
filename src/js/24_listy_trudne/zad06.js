/*

Tytul: Polaczone posortowane listy 

Tresc: Otrzymujesz liste zawierajaca M posortowanych list. Polacz te listy w jedna posortowana liste. Wszystkie elementy sa unikalne.

Dane wejsciowe: Lista list zawierajacych liczby naturalne.

Dane wyjsciowe: Lista zawierajaca liczby naturalne.

Przyklad:

Dla wejsciowej listy:
[[ -6, 23, 29, 33],
[ 6, 22, 35, 71 ],
[ 5, 19, 21, 37 ],
[ -12, -7, -3, 28 ]],

powinna zostac zwrocona lista: [-12, -7, -6, -3, 5, 6, 19, 21, 22, 23, 28, 29, 33, 35, 37, 71].

*/

const polaczListy = (lista) => {
  let result = [];
  for (let i = 0; i < lista.length; i++) {
    result = result.concat(lista[i]);
  }
  return result.sort((a, b) => a - b);
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

console.assert(
  JSON.stringify(polaczListy(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(polaczListy(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);

