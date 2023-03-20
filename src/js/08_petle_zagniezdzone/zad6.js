/*
Tytuł: Litera Z.

Treść: Napisz funkcję, która dla otrzymanej liczby naturalnej wypisze literę Z o wysokości równej tej liczbie.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Komunikat.

Przykład:

Dla otrzymanej liczby 5 powinno zostać wypisane:

    *****
        * 
       *
      *
    *****

*/

// Funkcja wypisująca literę Z o wysokości równej liczbie
function rysujZ(wysokosc) {
    var wiersz = '';
    for (var i = 0; i < wysokosc; i++) {
        for (var j = 0; j < wysokosc; j++) {
            if (i === 0 || i === wysokosc - 1 || i + j === wysokosc - 1) {
                wiersz += '*';
            } else {
                wiersz += ' ';
            }
        }
        console.log(wiersz);
        wiersz = '';
    }
}

// Testy
console.log('Rysuj literę Z o wysokości 2');
rysujZ(2);

console.log('\nRysuj literę Z o wysokości 3');
rysujZ(3);

console.log('\nRysuj literę Z o wysokości 4');
rysujZ(4);