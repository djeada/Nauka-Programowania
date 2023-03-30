/*

Tytul: Znalezienie elementu bez pary w liscie liczb calkowitych.

Tresc: Dla otrzymanej listy liczb calkowitych, skladajacej sie z nieparzystej liczby elementow, znajdz element, ktory nie ma pary o tej samej wartosci.

Dane wejsciowe: Lista liczb calkowitych.

Dane wyjsciowe: Liczba calkowita.

Przyklad:

Dla otrzymanej listy: [1, 3, 1, 7, 3, 1, 1] zostanie zwrocona liczba: 7.
*/

// Funkcja znajdujaca element bez pary w liscie liczb calkowitych
function znajdzElementBezPary(lista) {
  let bezPary = 0;
  for (let liczba of lista) {
    bezPary ^= liczba;
  }
  return bezPary;
}

// Testy

function testZnajdzElementBezPary() {
  console.assert(znajdzElementBezPary([1, 3, 1, 7, 3, 1, 1]) === 7);
  console.assert(znajdzElementBezPary([4, 4, 2, 2, 1]) === 1);
  console.assert(znajdzElementBezPary([9, 1, 1, 8, 9, 8]) === 0);
  console.assert(znajdzElementBezPary([3, 3, 6, 6, 5, 7, 7]) === 5);
}

testZnajdzElementBezPary();

