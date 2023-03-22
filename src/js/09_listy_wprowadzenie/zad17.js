/*

Tytuł: Znalezienie wszystkich par elementów listy o sumie równej podanej liczbie.

Treść: Dla otrzymanej listy liczb całkowitych oraz liczby x, znajdź wszystkie pary elementów listy, których suma jest równa x.

Dane wejściowe: Lista liczb całkowitych oraz liczba całkowita.

Dane wyjściowe: Lista par liczb całkowitych.

Przykład:

Dla otrzymanej listy: [1, 2, 4, 3, 7] oraz liczby 5, zostaną zwrócone wszystkie pary elementów o sumie równej 5: [(1, 4), (2, 3)].
*/

// Funkcja znajdująca wszystkie pary elementów o sumie równej podanej liczbie
function znajdzWszystkieParySumujaceDo(lista, x) {
  const mapaIndeksow = new Map();
  const pary = [];

  for (let i = 0; i < lista.length; i++) {
    const komplement = x - lista[i];
    if (mapaIndeksow.has(komplement)) {
      pary.push([komplement, lista[i]]);
    }
    mapaIndeksow.set(lista[i], i);
  }

  return pary;
}

// Testy
function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
}

function testZnajdzWszystkieParySumujaceDo() {
  assert(
    JSON.stringify(znajdzWszystkieParySumujaceDo([1, 2, 4, 3, 7], 5)) ===
      JSON.stringify([
        [1, 4],
        [2, 3],
      ])
  );
  assert(
    JSON.stringify(znajdzWszystkieParySumujaceDo([2, 5, 9, 4, 7], 12)) ===
      JSON.stringify([
        [5, 7],
        [9, 3],
      ])
  );
  assert(
    JSON.stringify(znajdzWszystkieParySumujaceDo([2, 5, 9, 4, 7], 20)) ===
      JSON.stringify([])
  );
}

testZnajdzWszystkieParySumujaceDo();
