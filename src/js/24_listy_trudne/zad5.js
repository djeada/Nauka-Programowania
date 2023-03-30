/*

Tytuł: Zbiór potęgowy 

Treść: Otrzymujesz listę liczb naturalnych. Zwróć zbiór potęgowy otrzymanej listy, czyli zbiór wszystkich jej podzbiorów.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Lista list zawierająca elementy z wejściowej listy lub pustą listę.

Przykład:

Dla wejściowej listy [1, 2, 1], powinna zostać zwrócona lista: [[], [1], [2], [1, 2], [1, 1], [1, 2, 1]].

*/
function zbiorPotegowy(lista) {
  // wymaga sortowania O(nlogn)
  lista.sort();

  const N = Math.pow(2, lista.length);
  const zbiorPotegowy = new Set();

  for (let i = 0; i < N; i++) {
    const subset = lista.filter((_, j) => i & (1 << j));
    zbiorPotegowy.add(JSON.stringify(subset));
  }

  return Array.from(zbiorPotegowy, JSON.parse);
}

// Testy
const lista1 = [1, 2, 1];
const wynik1 = [[], [1], [2], [1, 2], [1, 1], [1, 1, 2]];
const lista2 = [1, 2, 3, 4];
const wynik2 = [
  [],
  [1],
  [2],
  [1, 2],
  [3],
  [1, 3],
  [2, 3],
  [1, 2, 3],
  [4],
  [1, 4],
  [2, 4],
  [1, 2, 4],
  [3, 4],
  [1, 3, 4],
  [2, 3, 4],
  [1, 2, 3, 4],
];

const sortSubsets = (a, b) =>
  a.length - b.length || a.toString().localeCompare(b.toString());

const sortedResult1 = zbiorPotegowy(lista1).sort(sortSubsets);
const sortedExpected1 = wynik1.sort(sortSubsets);
const sortedResult2 = zbiorPotegowy(lista2).sort(sortSubsets);
const sortedExpected2 = wynik2.sort(sortSubsets);

console.assert(
  JSON.stringify(sortedResult1) === JSON.stringify(sortedExpected1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortedResult2) === JSON.stringify(sortedExpected2),
  "Test 2 nieudany"
);
