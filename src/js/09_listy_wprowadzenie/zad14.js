/*

Tytuł: Znalezienie elementu bez pary w liście liczb całkowitych.

Treść: Dla otrzymanej listy liczb całkowitych, składającej się z nieparzystej liczby elementów, znajdź element, który nie ma pary o tej samej wartości.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Liczba całkowita.

Przykład:

Dla otrzymanej listy: [1, 3, 1, 7, 3, 1, 1] zostanie zwrócona liczba: 7.
*/

// Funkcja znajdująca element bez pary w liście liczb całkowitych
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
