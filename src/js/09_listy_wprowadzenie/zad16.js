/*
Tytuł: Znalezienie indeksów pierwszej pary elementów listy o sumie równej podanej liczbie.

Treść: Dla otrzymanej listy liczb całkowitych oraz liczby x, znajdź indeksy pierwszej pary elementów listy, których suma jest równa x. Jeśli taka para nie istnieje, zwróć parę (-1, -1).

Dane wejściowe: Lista liczb całkowitych oraz liczba całkowita.

Dane wyjściowe: Para liczb całkowitych.

Przykład:

Dla otrzymanej listy: [1, 3, 4, 5, 2] oraz liczby 5, zostaną zwrócone indeksy pierwszej pary elementów o sumie równej 5: (0, 2).
*/

// Funkcja znajdująca indeksy pierwszej pary elementów o sumie równej podanej liczbie
function znajdzPareSumujacaDo(lista, x) {
  const mapaIndeksow = new Map();

  for (let i = 0; i < lista.length; i++) {
    const komplement = x - lista[i];
    if (mapaIndeksow.has(komplement)) {
      return [mapaIndeksow.get(komplement), i];
    }
    mapaIndeksow.set(lista[i], i);
  }

  return [-1, -1];
}

// Testy

function testZnajdzPareSumujacaDo() {
  console.assert(
    JSON.stringify(znajdzPareSumujacaDo([1, 3, 4, 5, 2], 5)) ===
      JSON.stringify([0, 2])
  );
  console.assert(
    JSON.stringify(znajdzPareSumujacaDo([2, 5, 9, 4, 7], 12)) ===
      JSON.stringify([1, 4])
  );
  console.assert(
    JSON.stringify(znajdzPareSumujacaDo([2, 5, 9, 4, 7], 20)) ===
      JSON.stringify([-1, -1])
  );
}

testZnajdzPareSumujacaDo();
