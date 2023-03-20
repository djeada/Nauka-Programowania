/*

Tytuł: Znalezienie brakującego elementu w liście.

Treść: Dla dostarczonej listy, składającej się z nieuporządkowanych kolejnych (oprócz jednego) elementów ciągu arytmetycznego, znajdź brakujący element.

Dane wejściowe: Lista zawierająca liczby naturalne.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej listy: [5, 2, 1, 3] zostanie zwrócona liczba: 4.
*/

// Funkcja znajdująca brakujący element w ciągu arytmetycznym
function znajdzBrakujacyElement(lista) {
    const n = lista.length + 1;
    const sumaKolejnychLiczb = (n * (n + 1)) / 2;
    const sumaListy = lista.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    return sumaKolejnychLiczb - sumaListy;
}

// Testy
function assert(condition, message) {
    if (!condition) {
        throw new Error(message || "Assertion failed");
    }
}

function testZnajdzBrakujacyElement() {
    assert(znajdzBrakujacyElement([5, 2, 1, 3]) === 4);
    assert(znajdzBrakujacyElement([1, 3, 4, 5, 6]) === 2);
    assert(znajdzBrakujacyElement([1, 2, 4]) === 3);
    assert(znajdzBrakujacyElement([3, 5, 6, 7, 8]) === 4);
}

testZnajdzBrakujacyElement();