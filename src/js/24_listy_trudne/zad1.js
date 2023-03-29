/*

Tytuł: Najdłuższy ciąg jedynek.

Treść: Otrzymujesz listę składającą się wyłącznie z zer i jedynek. Znajdź indeks zera, które po zamianie na jedynkę dałoby najdłuższy ciąg jedynek. Jeśli lista składa się wyłącznie z zer lub wyłącznie z jedynek, zwróć -1.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej listy: [0, 0, 1, 0, 1, 1, 1, 0, 1, 1], powinna zostać zwrócona liczba: 7.

*/

const najdluzszyCiągJedynek = (lista) => {
  let najdluzszyCiągJedynek = 0;
  let index = -1;
  let liczbaJedynek = 0;
  let indeks = 0;
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] === 1) {
      liczbaJedynek++;
    } else {
      indeks = i;
    }
    if (liczbaJedynek > najdluzszyCiągJedynek) {
      najdluzszyCiągJedynek = liczbaJedynek;
      index = indeks;
    }
  }
  return index;
};

const assert = (condition, message) => {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
};

// Testy
const lista1 = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1];
const wynik1 = 7;
const lista2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
const wynik2 = -1;

assert(najdluzszyCiągJedynek(lista1) === wynik1, "Test 1 nieudany");
assert(najdluzszyCiągJedynek(lista2) === wynik2, "Test 2 nieudany");
