/*
Tytul: Litera X.

Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze litere X o wysokosci rownej tej liczbie.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Komunikat.

Przyklad:

Dla otrzymanej liczby 4 powinno zostac wypisane:

    *   *
     * *
     * *
    *   *

*/

// Funkcja wypisujaca litere X o wysokosci rownej liczbie
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
console.log("Rysuj litere X o wysokosci 2");
rysujX(2);

console.log("\nRysuj litere X o wysokosci 3");
rysujX(3);

console.log("\nRysuj litere X o wysokosci 4");
rysujX(4);

