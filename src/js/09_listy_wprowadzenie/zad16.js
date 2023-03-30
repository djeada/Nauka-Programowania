/*
Tytul: Znalezienie indeksow pierwszej pary elementow listy o sumie rownej podanej liczbie.

Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby x, znajdz indeksy pierwszej pary elementow listy, ktorych suma jest rowna x. Jesli taka para nie istnieje, zwroc pare (-1, -1).

Dane wejsciowe: Lista liczb calkowitych oraz liczba calkowita.

Dane wyjsciowe: Para liczb calkowitych.

Przyklad:

Dla otrzymanej listy: [1, 3, 4, 5, 2] oraz liczby 5, zostana zwrocone indeksy pierwszej pary elementow o sumie rownej 5: (0, 2).
*/

// Funkcja znajdujaca indeksy pierwszej pary elementow o sumie rownej podanej liczbie
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

