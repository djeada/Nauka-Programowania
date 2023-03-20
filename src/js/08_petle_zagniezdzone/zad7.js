/*
Tytuł: Choinka.

Treść: Napisz funkcję, która dla otrzymanej liczby naturalnej N, wypisze N trójkątów ustawionych w kolumnie, jeden na drugim. Wysokość pierwszego trójkąta to 1, a każdego następnego jest równa wysokości poprzedniego powiększonej o 1.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Komunikat.

Przykład:

Dla otrzymanej liczby 3 powinno zostać wypisane:

    *
    *
    **
    *
    **
    ***
    */

// Funkcja wypisująca N trójkątów ustawionych w kolumnie
function rysujChoinke(n) {
    var wiersz = '';
    for (var i = 0; i < n; i++) {
        for (var j = 0; j <= i; j++) {
            wiersz += '*';
            console.log(wiersz);
        }
        wiersz = '';
    }
}

// Testy
console.log('Rysuj choinkę o wysokości 2');
rysujChoinke(2);

console.log('\nRysuj choinkę o wysokości 3');
rysujChoinke(3);

console.log('\nRysuj choinkę o wysokości 4');
rysujChoinke(4);