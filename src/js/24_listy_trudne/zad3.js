/*

Tytuł: Minimalny iloczyn.

Treść: Otrzymujesz listę liczb całkowitych. Znajdź najmniejszy iloczyn dla trzech liczb wybranych z listy. Jeśli lista składa się z mniej niż trzech liczb, zwróć iloczyn wszystkich elementów listy.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Liczba całkowita.

Przykład:

Dla otrzymanej listy: [3, -1, -3, 2, 9, 4], powinna zostać zwrócona liczba: -108.

*/

const minimalnyIloczyn = (lista) => {
  let min = lista[0] * lista[1] * lista[2];
  for (let i = 0; i < lista.length; i++) {
    for (let j = i + 1; j < lista.length; j++) {
      for (let k = j + 1; k < lista.length; k++) {
        if (lista[i] * lista[j] * lista[k] < min) {
          min = lista[i] * lista[j] * lista[k];
        }
      }
    }
  }
  return min;
};

const assert = (condition, message) => {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
};

// Testy
const lista1 = [3, -1, -3, 2, 9, 4];
const wynik1 = -108;
const lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const wynik2 = 6;

assert(minimalnyIloczyn(lista1) === wynik1, "Test 1 nieudany");
assert(minimalnyIloczyn(lista2) === wynik2, "Test 2 nieudany");
