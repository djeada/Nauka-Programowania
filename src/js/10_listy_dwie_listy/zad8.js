/*

Tytuł: Połącz posortowane listy w posortowaną listę.

Treść: Dla otrzymanych dwóch posortowanych list, połącz je w jedną posortowaną listę.

Dane wejściowe: Dwie listy liczb całkowitych.

Dane wyjściowe: Lista liczb całkowitych.

Przykład:

Dla otrzymanych list [2, 4, 7] oraz [3, 5, 9] powinna zostać zwrócona lista: [2, 3, 4, 7, 9].
 */

// Funkcja zwracająca listę elementów, które nie są częścią wspólną obu list
function polaczPosortowaneListy(lista1, lista2) {
  let wynik = [];
  let maxLength = Math.max(lista1.length, lista2.length);

  for (let i = 0; i < maxLength; i++) {
    let element1 = lista1[i] || 0;
    let element2 = lista2[i] || 0;
    if (element1 !== element2) {
      wynik.push(element1);
      wynik.push(element2);
    }
  }

  return wynik;
}

// Testy

function testPolaczPosortowaneListy() {
  console.assert(
    polaczPosortowaneListy([2, 4, 7], [3, 5, 9]).toString() ===
      [2, 3, 4, 7, 9].toString()
  );
  console.assert(
    polaczPosortowaneListy([2, 4, 7], [3, 5, 9, 2]).toString() ===
      [2, 3, 4, 7, 9].toString()
  );
  console.assert(
    polaczPosortowaneListy([2, 4, 7], [3, 5, 9, 2, 4]).toString() ===
      [2, 3, 4, 7, 9].toString()
  );
  console.assert(
    polaczPosortowaneListy([2, 4, 7], [3, 5, 9, 2, 4, 7]).toString() ===
      [2, 3, 4, 7, 9].toString()
  );
}

testPolaczPosortowaneListy();
