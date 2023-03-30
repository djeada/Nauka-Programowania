/*

Tytul: Znalezienie elementow wspolnych dwoch list.

Tresc: Otrzymujesz dwie listy liczb calkowitych. Znajdz elementy wystepujace zarowno w pierwszej, jak i w drugiej liscie.

Dane wejsciowe: Dwie listy liczb calkowitych.

Dane wyjsciowe: Lista liczb calkowitych.

Przyklad:

Dla otrzymanych list [9, 2, 5, 4] oraz [4, 2, 1] zostanie zwrocona lista: [2, 4].

*/

// Funkcja zwracajaca liste elementow wystepujacych zarowno w pierwszej, jak i w drugiej liscie
function znajdzElementyWspolne(lista1, lista2) {
  let wynik = [];
  let maxLength = Math.max(lista1.length, lista2.length);

  for (let i = 0; i < maxLength; i++) {
    let element1 = lista1[i] || 0;
    let element2 = lista2[i] || 0;
    if (element1 === element2) {
      wynik.push(element1);
    }
  }

  return wynik;
}

// Testy

function testZnajdzElementyWspolne() {
  console.assert(
    znajdzElementyWspolne([9, 2, 5, 4], [4, 2, 1]).toString() ===
      [2, 4].toString()
  );
  console.assert(
    znajdzElementyWspolne([9, 2, 5, 4], [4, 2, 1, 9]).toString() ===
      [2, 4, 9].toString()
  );
  console.assert(
    znajdzElementyWspolne([9, 2, 5, 4], [4, 2, 1, 9, 5]).toString() ===
      [2, 4, 5, 9].toString()
  );
  console.assert(
    znajdzElementyWspolne([9, 2, 5, 4], [4, 2, 1, 9, 5, 2]).toString() ===
      [2, 4, 5, 9].toString()
  );
}

testZnajdzElementyWspolne();

