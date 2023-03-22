/*
Tytuł: Litera X.

Treść: Napisz funkcję, która dla otrzymanej liczby naturalnej wypisze literę X o wysokości równej tej liczbie.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Komunikat.

Przykład:

Dla otrzymanej liczby 4 powinno zostać wypisane:

    *   *
     * *
     * *
    *   *

*/

// Funkcja wypisująca literę X o wysokości równej liczbie
function rysujX(wysokosc) {
  var wiersz = "";
  for (var i = 0; i < wysokosc; i++) {
    for (var j = 0; j < wysokosc; j++) {
      if (i === j || i + j === wysokosc - 1) {
        wiersz += "*";
      } else {
        wiersz += " ";
      }
    }
    console.log(wiersz);
    wiersz = "";
  }
}

// Testy
console.log("Rysuj literę X o wysokości 2");
rysujX(2);

console.log("\nRysuj literę X o wysokości 3");
rysujX(3);

console.log("\nRysuj literę X o wysokości 4");
rysujX(4);
