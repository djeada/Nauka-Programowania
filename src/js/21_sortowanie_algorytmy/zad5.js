/*

Tytuł: Sortowanie szybkie.

Treść: Dla danej listy liczb całkowitych zaimplementuj algorytm sortowania szybkiego.

1. Jeśli długość listy jest mniejsza niż 2, zwróć listę.
2. Wybierz element rozdzielający, nazywany pivotem.
3. Podziel listę na trzy części: elementy mniejsze od pivota, pivot oraz elementy większe od pivota.
4. Wywołaj rekurencyjnie sortowanie szybkie dla części z elementami mniejszymi od pivota i większymi od pivota.
5. Scal posortowane części listy w jedną posortowaną listę.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Posortowana lista liczb całkowitych.

Przykład:

Dla danej listy: [6, 2, 1, 4, 27], powinna zostać zwrócona lista: [1, 2, 4, 6, 27].

*/

const sortowanieSzybkie = (lista) => {
  if (lista.length < 2) {
    return lista;
  }

  const pivotIndeks = Math.floor(Math.random() * lista.length);
  const pivot = lista[pivotIndeks];

  const mniejsze = [];
  const wieksze = [];
  const pivots = [];

  for (const element of lista) {
    if (element < pivot) {
      mniejsze.push(element);
    } else if (element > pivot) {
      wieksze.push(element);
    } else {
      pivots.push(element);
    }
  }

  return sortowanieSzybkie(mniejsze)
    .concat(pivots)
    .concat(sortowanieSzybkie(wieksze));
};

const assert = (condition, message) => {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
};

// Testy
const lista1 = [6, 2, 1, 4, 27];
const wynik1 = [1, 2, 4, 6, 27];
const lista2 = [5, 4, 3, 2, 1];
const wynik2 = [1, 2, 3, 4, 5];
const lista3 = [-3, 0, 15, -7, 23];
const wynik3 = [-7, -3, 0, 15, 23];

assert(
  JSON.stringify(sortowanieSzybkie(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
assert(
  JSON.stringify(sortowanieSzybkie(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
assert(
  JSON.stringify(sortowanieSzybkie(lista3)) === JSON.stringify(wynik3),
  "Test 3 nieudany"
);
