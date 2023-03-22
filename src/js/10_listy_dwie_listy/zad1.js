/*

Tytuł: Wypisanie elementów dwóch list na przemian.

Treść: Dla otrzymanych dwóch list, wypisuj na przemian elementy z obu list. Jeśli listy nie są tej samej długości, po wyczerpaniu elementów krótszej listy, wypisuj pozostałe elementy dłuższej listy.

Dane wejściowe: Dwie listy.

Dane wyjściowe: Kilka liczb.

Przykład:

Dla otrzymanych list [5, 3, 7, 2] oraz [1, -2, 3], zostaną wypisane: 5, 1, 3, -2, 7, 3, 2.
*/

// Funkcja wypisująca elementy dwóch list na przemian
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
