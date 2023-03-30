/*

Tytuł: Znalezienie elementu dominującego w liście liczb naturalnych.

Treść: Dla dostarczonej listy liczb naturalnych, znajdź element, który występuje w niej więcej niż połowa jej długości. Jeśli taki element nie istnieje, zwróć -1.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej listy: [4, 7, 4, 4, 2] zostanie zwrócona liczba: 4.
*/

// Funkcja znajdująca element dominujący w liście liczb naturalnych
function znajdzElementDominujacy(lista) {
  let kandydat = null;
  let licznik = 0;

  for (let liczba of lista) {
    if (licznik === 0) {
      kandydat = liczba;
    }
    licznik += kandydat === liczba ? 1 : -1;
  }

  let wystapienia = lista.filter((liczba) => liczba === kandydat).length;
  return wystapienia > lista.length / 2 ? kandydat : -1;
}

// Testy

function testZnajdzElementDominujacy() {
  console.assert(znajdzElementDominujacy([4, 7, 4, 4, 2]) === 4);
  console.assert(znajdzElementDominujacy([2, 2, 1, 1, 3]) === -1);
  console.assert(znajdzElementDominujacy([5, 5, 5, 3, 3, 5, 5]) === 5);
  console.assert(znajdzElementDominujacy([6, 6, 6, 2, 6, 6]) === 6);
}

testZnajdzElementDominujacy();
