/*
Tytuł: Usuń klucz.

Treść: Dla otrzymanej listy: liczb całkowitych oraz klucza, usuń pierwsze wystąpienie klucza w liście.

Dane wejściowe: Lista liczb całkowitych i liczba całkowita.

Dane wyjściowe: Lista liczb całkowitych.

Przykład:

Dla otrzymanej listy: [6, 2, 1, 4, 27] oraz 4, powinna zostać zwrócona lista: [6, 2, 1, 27].

*/

function usunKlucz(lista, klucz) {
    let wynik = [];
    let czyZnaleziono = false;
    for (let i = 0; i < lista.length; i++) {
        if (lista[i] === klucz && !czyZnaleziono) {
            czyZnaleziono = true;
        } else {
            wynik.push(lista[i]);
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

function testUsunKlucz() {
    assert(usunKlucz([6, 2, 1, 4, 27], 4).toString() === [6, 2, 1, 27].toString());
    assert(usunKlucz([6, 2, 1, 4, 27], 6).toString() === [2, 1, 4, 27].toString());
    assert(usunKlucz([6, 2, 1, 4, 27], 27).toString() === [6, 2, 1, 4].toString());
}

function main() {
    testUsunKlucz();
}

main();