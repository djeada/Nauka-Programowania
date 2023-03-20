/*

Tytuł: Usuń z pierwszej listy część wspólną obu list.

Treść: Otrzymujesz dwie listy liczb całkowitych. Usuń z pierwszej listy te elementy, które występują również w drugiej liście.

Dane wejściowe: Dwie listy liczb całkowitych.

Dane wyjściowe: Lista liczb całkowitych.

Przykład:

Dla otrzymanych list [9, 2, 5, 4] oraz [4, 2, 1] powinna zostać zwrócona lista: [9, 5].
*/

// Funkcja zwracająca listę elementów, które nie są częścią wspólną obu list
function usunCzescWspolna(lista1, lista2) {
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
function assert(condition, message) {
    if (!condition) {
        throw new Error(message || "Assertion failed");
    }
}

function testUsunCzescWspolna() {
    assert(usunCzescWspolna([9, 2, 5, 4], [4, 2, 1]).toString() === [9, 5].toString());
    assert(usunCzescWspolna([9, 2, 5, 4], [4, 2, 1, 9]).toString() === [5].toString());
    assert(usunCzescWspolna([9, 2, 5, 4], [4, 2, 1, 9, 5]).toString() === [1].toString());
    assert(usunCzescWspolna([9, 2, 5, 4], [4, 2, 1, 9, 5, 2]).toString() === [1].toString());
}


testUsunCzescWspolna()