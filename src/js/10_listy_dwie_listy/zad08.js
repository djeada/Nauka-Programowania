/*

Tytul: Polacz posortowane listy w posortowana liste.

Tresc: Dla otrzymanych dwoch posortowanych list, polacz je w jedna posortowana liste.

Dane wejsciowe: Dwie listy liczb calkowitych.

Dane wyjsciowe: Lista liczb calkowitych.

Przyklad:

Dla otrzymanych list [2, 4, 7] oraz [3, 5, 9] powinna zostac zwrocona lista: [2, 3, 4, 7, 9].
 */

// Funkcja zwracajaca liste elementow, ktore nie sa czescia wspolna obu list
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

