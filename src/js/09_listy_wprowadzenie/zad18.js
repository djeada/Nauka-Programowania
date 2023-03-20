/*
Tytuł: Znalezienie indeksu najmniejszego elementu w posortowanej i przesuniętej w prawo liście.

Treść: Dla otrzymanej listy liczb całkowitych, znajdź indeks najmniejszego elementu. Lista jest posortowana rosnąco, ale została przesunięta w prawo o określoną liczbę miejsc. Przykładowo dla przesunięcia w prawo o 1, ostatni element trafia na pierwsze miejsce, a przedostatni na ostatnie miejsce itd.

Dane wejściowe: Lista liczb całkowitych oraz liczba naturalna określająca przesunięcie w prawo.

Dane wyjściowe: Liczba całkowita.

Przykład:

Dla otrzymanej listy: [7, 8, -1, 4, 5] zostanie zwrócona liczba: 2.
*/

// Funkcja znajdująca indeks najmniejszego elementu w posortowanej i przesuniętej w prawo liście
function znajdzIndeksNajmniejszegoElementu(lista) {
    let indeksNajmniejszego = 0;

    for (let i = 1; i < lista.length; i++) {
        if (lista[i] < lista[indeksNajmniejszego]) {
            indeksNajmniejszego = i;
        }
    }

    return indeksNajmniejszego;
}

// Testy
function assert(condition, message) {
    if (!condition) {
        throw new Error(message || "Assertion failed");
    }
}

function testZnajdzIndeksNajmniejszegoElementu() {
    assert(znajdzIndeksNajmniejszegoElementu([7, 8, -1, 4, 5]) === 2);
    assert(znajdzIndeksNajmniejszegoElementu([4, 5, 7, 8, -1]) === 4);
    assert(znajdzIndeksNajmniejszegoElementu([-1, 4, 5, 7, 8]) === 0);
}

testZnajdzIndeksNajmniejszegoElementu();