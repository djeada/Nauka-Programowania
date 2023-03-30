/*
Tytul: Trojkat prostokatny rownoboczny

Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze trojkat prostokatny rownoboczny o wysokosci rownej tej liczbie.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Komunikat.

Przyklad:

Dla otrzymanej liczby 3 powinno zostac wypisane:

    *
    **
    ***

*/

// Funkcja wypisujaca trojkat prostokatny rownoboczny o wysokosci rownej liczbie
function rysujTrojkat(wysokosc) {
  var wiersz = "";
  for (var i = 0; i < wysokosc; i++) {
    wiersz += "*";
    console.log(wiersz);
  }
}

// Testy
console.log("Rysuj trojkat prostokatny rownoboczny o wysokosci 2");
rysujTrojkat(2);

console.log("\nRysuj trojkat prostokatny rownoboczny o wysokosci 3");
rysujTrojkat(3);

console.log("\nRysuj trojkat prostokatny rownoboczny o wysokosci 4");
rysujTrojkat(4);

