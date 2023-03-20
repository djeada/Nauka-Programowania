/*

Tytuł: Liczba mniejsza od największej i większa od wszystkich pozostałych.

Treść: Otrzymujesz listę liczb naturalnych. Znajdź największą i drugą co do wielkości liczbę w liście, a następnie oblicz średnią arytmetyczną tych dwóch liczb i zwróć ją jako liczbę zmiennoprzecinkową.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Liczba zmiennoprzecinkowa oznaczająca średnią arytmetyczną największej i drugiej co do wielkości liczby z listy.

Przykład:

Dla otrzymanej listy [9, 2, 3, 2, 1, 7] powinna zostać zwrócona liczba 8.0.
    
    */

function liczbaMniejszaOdNajwiekszej(lista) {
    let max = lista[0];
    let secondMax = lista[0];
    for (let i = 1; i < lista.length; i++) {
        if (lista[i] > max) {
            secondMax = max;
            max = lista[i];
        } else if (lista[i] > secondMax) {
            secondMax = lista[i];
        }
    }
    return (max + secondMax) / 2;
}

// Testy
function assert(condition, message) {
    if (!condition) {
        throw new Error(message || "Assertion failed");
    }
}

function testLiczbaMniejszaOdNajwiekszej() {
    assert(liczbaMniejszaOdNajwiekszej([9, 2, 3, 2, 1, 7]) === 8.0);
    assert(liczbaMniejszaOdNajwiekszej([1, 2, 3, 4, 5, 6]) === 5.5);
    assert(liczbaMniejszaOdNajwiekszej([6, 5, 4, 3, 2, 1]) === 3.5);
}

function main() {
    testLiczbaMniejszaOdNajwiekszej();
}

main();