/*

Tytuł: Sortowanie bąbelkowe.

Treść: Napisz program sortujący listę liczb całkowitych metodą sortowania bąbelkowego. Porównaj sąsiednie liczby z listy i zamień je miejscami, jeśli pierwsza jest większa od drugiej. Powtarzaj operację, aż przejdziesz przez całą listę bez dokonywania zmian.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Posortowana lista liczb całkowitych.

Przykład:

Dla listy: [6, 2, 1, 4, 27], powinna zostać zwrócona lista: [1, 2, 4, 6, 27].

*/

const sortowanieBabelkowe = (lista) => {
  let zamiana;
  do {
    zamiana = false;
    for (let i = 0; i < lista.length - 1; i++) {
      if (lista[i] > lista[i + 1]) {
        [lista[i], lista[i + 1]] = [lista[i + 1], lista[i]];
        zamiana = true;
      }
    }
  } while (zamiana);
  return lista;
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
  JSON.stringify(sortowanieBabelkowe(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
assert(
  JSON.stringify(sortowanieBabelkowe(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
assert(
  JSON.stringify(sortowanieBabelkowe(lista3)) === JSON.stringify(wynik3),
  "Test 3 nieudany"
);
