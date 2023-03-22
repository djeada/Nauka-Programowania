/*
Tytuł: Odwrócony trójkąt prostokątny równoboczny

Treść: Napisz funkcję, która dla otrzymanej liczby naturalnej wypisze, zaczynając od podstawy, trójkąt prostokątny równoboczny o wysokości równej tej liczbie.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Komunikat.

Przykład:

Dla otrzymanej liczby 4 powinno zostać wypisane:

    ****
    ***
    **
    *

*/

// Funkcja wypisująca odwrócony trójkąt prostokątny równoboczny o wysokości równej liczbie
function rysujTrojkat(wysokosc) {
  var wiersz = "";
  for (var i = 0; i < wysokosc; i++) {
    for (var j = 0; j < wysokosc - i; j++) {
      wiersz += "*";
    }
    console.log(wiersz);
    wiersz = "";
  }
}

// Testy
console.log("Rysuj odwrócony trójkąt prostokątny równoboczny o wysokości 2");
rysujTrojkat(2);

console.log("\nRysuj odwrócony trójkąt prostokątny równoboczny o wysokości 3");
rysujTrojkat(3);

console.log("\nRysuj odwrócony trójkąt prostokątny równoboczny o wysokości 4");
rysujTrojkat(4);
