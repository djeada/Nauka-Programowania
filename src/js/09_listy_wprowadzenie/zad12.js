/*

Tytul: Rotacja w lewo/prawo.

Tresc: Otrzymujesz liste liczb calkowitych, kierunek przesuniecia (1 odpowiada przesunieciu w prawo, a 0 w lewo) oraz liczbe miejsc, o jaka elementy listy maja zostac przesuniete. Na przyklad dla przesuniecia w prawo, pierwszy element trafia na drugie miejsce, drugi na trzecie, a ostatni na pierwsze miejsce. Przesun elementy listy w podanym kierunku.

Dane wejsciowe: Lista liczb calkowitych oraz dwie liczby naturalne.

Dane wyjsciowe: Lista liczb calkowitych.

Przyklad:

Dla otrzymanej listy: [5, 27, 6, 2, 1, 10, 8] oraz liczb 0 i 2, powinna zostac zwrocona lista: [6, 2, 1, 10, 8, 5, 27].
*/

// Funkcja rotujaca elementy listy o podana liczbe miejsc
function rotacjaListy(lista, kierunek, przesuniecie) {
  przesuniecie %= lista.length;

  if (kierunek === 1) {
    // Rotacja w prawo
    return lista.slice(-przesuniecie).concat(lista.slice(0, -przesuniecie));
  } else {
    // Rotacja w lewo
    return lista.slice(przesuniecie).concat(lista.slice(0, przesuniecie));
  }
}

// Testy

function testRotacjaListy() {
  const lista1 = [5, 27, 6, 2, 1, 10, 8];
  console.assert(
    JSON.stringify(rotacjaListy(lista1, 0, 2)) ===
      JSON.stringify([6, 2, 1, 10, 8, 5, 27])
  );
  console.assert(
    JSON.stringify(rotacjaListy(lista1, 1, 2)) ===
      JSON.stringify([10, 8, 5, 27, 6, 2, 1])
  );
}

testRotacjaListy();

