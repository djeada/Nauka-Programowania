/*

Tytul: Znalezienie elementu dominujacego w liscie liczb naturalnych.

Tresc: Dla dostarczonej listy liczb naturalnych, znajdz element, ktory wystepuje w niej wiecej niz polowa jej dlugosci. Jesli taki element nie istnieje, zwroc -1.

Dane wejsciowe: Lista liczb naturalnych.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanej listy: [4, 7, 4, 4, 2] zostanie zwrocona liczba: 4.
*/

// Funkcja znajdujaca element dominujacy w liscie liczb naturalnych
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

