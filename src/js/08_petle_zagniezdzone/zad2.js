/*
Tytuł: Trójkąt prostokątny równoboczny

Treść: Napisz funkcję, która dla otrzymanej liczby naturalnej wypisze trójkąt prostokątny równoboczny o wysokości równej tej liczbie.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Komunikat.

Przykład:

Dla otrzymanej liczby 3 powinno zostać wypisane:

    *
    **
    ***

*/

// Funkcja wypisująca trójkąt prostokątny równoboczny o wysokości równej liczbie
function rysujTrojkat(wysokosc) {
    var wiersz = '';
    for (var i = 0; i < wysokosc; i++) {
        wiersz += '*';
        console.log(wiersz);
    }
}

// Testy
console.log('Rysuj trójkąt prostokątny równoboczny o wysokości 2');
rysujTrojkat(2);

console.log('\nRysuj trójkąt prostokątny równoboczny o wysokości 3');
rysujTrojkat(3);

console.log('\nRysuj trójkąt prostokątny równoboczny o wysokości 4');
rysujTrojkat(4);