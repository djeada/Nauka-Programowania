/*
Tytuł: Tabliczka mnożenia.

Treść: Napisz funkcję, która dla otrzymanej liczby naturalnej N, wypisze N pierwszych wierszy i kolumn tabliczki mnożenia.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Wiersze i kolumny tabliczki mnożenia o wymiarach NxN.

Przykład:

Dla otrzymanej liczby 3 powinno zostać wypisane:

    1 2 3
    2 4 6
    3 6 9

    */

// Funkcja wypisująca tabliczkę mnożenia o wymiarach NxN
function tabliczkaMnozenia(n) {
    for (var i = 1; i <= n; i++) {
        var wiersz = '';
        for (var j = 1; j <= n; j++) {
            wiersz += i * j + ' ';
        }
        console.log(wiersz);
    }
}

// Testy
console.log('Tabliczka mnożenia o wymiarach 2x2');
tabliczkaMnozenia(2);

console.log('\nTabliczka mnożenia o wymiarach 3x3');
tabliczkaMnozenia(3);

console.log('\nTabliczka mnożenia o wymiarach 4x4');
tabliczkaMnozenia(4);