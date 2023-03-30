/*

Tytul: Wypisanie elementow dwoch list na przemian.

Tresc: Dla otrzymanych dwoch list, wypisuj na przemian elementy z obu list. Jesli listy nie sa tej samej dlugosci, po wyczerpaniu elementow krotszej listy, wypisuj pozostale elementy dluzszej listy.

Dane wejsciowe: Dwie listy.

Dane wyjsciowe: Kilka liczb.

Przyklad:

Dla otrzymanych list [5, 3, 7, 2] oraz [1, -2, 3], zostana wypisane: 5, 1, 3, -2, 7, 3, 2.
*/

// Funkcja wypisujaca elementy dwoch list na przemian
function wypiszElementyNaPrzemian(lista1, lista2) {
  let maxLength = Math.max(lista1.length, lista2.length);

  for (let i = 0; i < maxLength; i++) {
    if (i < lista1.length) {
      console.log(lista1[i]);
    }
    if (i < lista2.length) {
      console.log(lista2[i]);
    }
  }
}

// Testy
console.log("Test dla list [5, 3, 7, 2] oraz [1, -2, 3]:");
wypiszElementyNaPrzemian([5, 3, 7, 2], [1, -2, 3]);

