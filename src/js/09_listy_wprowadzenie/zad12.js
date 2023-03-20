/*

Tytuł: Rotacja w lewo/prawo.

Treść: Otrzymujesz listę liczb całkowitych, kierunek przesunięcia (1 odpowiada przesunięciu w prawo, a 0 w lewo) oraz liczbę miejsc, o jaką elementy listy mają zostać przesunięte. Na przykład dla przesunięcia w prawo, pierwszy element trafia na drugie miejsce, drugi na trzecie, a ostatni na pierwsze miejsce. Przesuń elementy listy w podanym kierunku.

Dane wejściowe: Lista liczb całkowitych oraz dwie liczby naturalne.

Dane wyjściowe: Lista liczb całkowitych.

Przykład:

Dla otrzymanej listy: [5, 27, 6, 2, 1, 10, 8] oraz liczb 0 i 2, powinna zostać zwrócona lista: [6, 2, 1, 10, 8, 5, 27].
*/

// Funkcja rotująca elementy listy o podaną liczbę miejsc
function rotacjaListy(lista, kierunek, przesuniecie) {
    przesuniecie %= lista.length;

    if (kierunek === 1) { // Rotacja w prawo
        return lista.slice(-przesuniecie).concat(lista.slice(0, -przesuniecie));
    } else { // Rotacja w lewo
        return lista.slice(przesuniecie).concat(lista.slice(0, przesuniecie));
    }
}

// Testy
function assert(condition, message) {
    if (!condition) {
        throw new Error(message || "Assertion failed");
    }
}

function testRotacjaListy() {
    const lista1 = [5, 27, 6, 2, 1, 10, 8];
    assert(JSON.stringify(rotacjaListy(lista1, 0, 2)) === JSON.stringify([6, 2, 1, 10, 8, 5, 27]));
    assert(JSON.stringify(rotacjaListy(lista1, 1, 2)) === JSON.stringify([10, 8, 5, 27, 6, 2, 1]));
}

testRotacjaListy();