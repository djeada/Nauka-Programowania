/*

Tytuł: Połączenie dwóch list.

Treść: Dla otrzymanych dwóch list, zwróć listę, która powstała poprzez:

a) Dostawienie drugiej listy na koniec pierwszej listy.
b) Wstawienie elementów o indeksach parzystych z drugiej listy na odpowiadające im indeksy pierwszej listy.

Dane wejściowe: Dwie listy.

Dane wyjściowe: Lista.

Przykład:

Dla otrzymanych list [1, 2, 3] oraz [4, 5, 6], w podpunkcie a) powinna zostać zwrócona lista: [1, 2, 3, 4, 5, 6].

W podpunkcie b) powinna zostać zwrócona lista: [4, 2, 6, 3].

*/

function polaczListy(lista1, lista2) {
    var wynik = [];
    for (var i = 0; i < lista1.length; i++) {
        wynik.push(lista1[i]);
    }
    for (var i = 0; i < lista2.length; i++) {
        wynik.push(lista2[i]);
    }
    return wynik;
}

function polaczListy2(lista1, lista2) {
    var wynik = [];
    for (var i = 0; i < lista1.length; i++) {
        if (i % 2 === 0) {
            wynik.push(lista2[i]);
        } else {
            wynik.push(lista1[i]);
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

function testPolaczListy() {
    assert(polaczListy([1, 2, 3], [4, 5, 6]).toString() === [1, 2, 3, 4, 5, 6].toString());
    assert(polaczListy([1, 2, 3], [4, 5, 6, 7, 8]).toString() === [1, 2, 3, 4, 5, 6, 7, 8].toString());
}

function testPolaczListy2() {
    assert(polaczListy2([1, 2, 3], [4, 5, 6]).toString() === [4, 2, 6].toString());
    assert(polaczListy2([1, 2, 3], [4, 5, 6, 7, 8]).toString() === [4, 2, 6].toString());
}

function main() {
    testPolaczListy();
    testPolaczListy2();
}

main();