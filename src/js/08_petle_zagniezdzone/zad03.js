/*
Tytul: Odwrocony trojkat prostokatny rownoboczny

Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze, zaczynajac od podstawy, trojkat prostokatny rownoboczny o wysokosci rownej tej liczbie.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Komunikat.

Przyklad:

Dla otrzymanej liczby 4 powinno zostac wypisane:

    ****
    ***
    **
    *

*/

// Funkcja wypisujaca odwrocony trojkat prostokatny rownoboczny o wysokosci rownej liczbie
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
console.log("Rysuj odwrocony trojkat prostokatny rownoboczny o wysokosci 2");
rysujTrojkat(2);

console.log("\nRysuj odwrocony trojkat prostokatny rownoboczny o wysokosci 3");
rysujTrojkat(3);

console.log("\nRysuj odwrocony trojkat prostokatny rownoboczny o wysokosci 4");
rysujTrojkat(4);

