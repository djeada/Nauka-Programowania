/*

Tytul: Znalezienie wszystkich par elementow listy o sumie rownej podanej liczbie.

Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby x, znajdz wszystkie pary elementow listy, ktorych suma jest rowna x.

Dane wejsciowe: Lista liczb calkowitych oraz liczba calkowita.

Dane wyjsciowe: Lista par liczb calkowitych.

Przyklad:

Dla otrzymanej listy: [1, 2, 4, 3, 7] oraz liczby 5, zostana zwrocone wszystkie pary elementow o sumie rownej 5: [(1, 4), (2, 3)].
*/

// Funkcja znajdujaca wszystkie pary elementow o sumie rownej podanej liczbie
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

function testZnajdzWszystkieParySumujaceDo() {
  console.assert(
    JSON.stringify(znajdzWszystkieParySumujaceDo([1, 2, 4, 3, 7], 5)) ===
      JSON.stringify([
        [1, 4],
        [2, 3],
      ])
  );
  console.assert(
    JSON.stringify(znajdzWszystkieParySumujaceDo([2, 5, 9, 4, 7], 12)) ===
      JSON.stringify([
        [5, 7],
        [9, 3],
      ])
  );
  console.assert(
    JSON.stringify(znajdzWszystkieParySumujaceDo([2, 5, 9, 4, 7], 20)) ===
      JSON.stringify([])
  );
}

testZnajdzWszystkieParySumujaceDo();

