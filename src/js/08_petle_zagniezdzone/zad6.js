/*
Tytul: Litera Z.

Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze litere Z o wysokosci rownej tej liczbie.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Komunikat.

Przyklad:

Dla otrzymanej liczby 5 powinno zostac wypisane:

    *****
        * 
       *
      *
    *****

*/

// Funkcja wypisujaca litere Z o wysokosci rownej liczbie
function rysujZ(wysokosc) {
  var wiersz = "";
  for (var i = 0; i < wysokosc; i++) {
    for (var j = 0; j < wysokosc; j++) {
      if (i === 0 || i === wysokosc - 1 || i + j === wysokosc - 1) {
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
console.log("Rysuj litere Z o wysokosci 2");
rysujZ(2);

console.log("\nRysuj litere Z o wysokosci 3");
rysujZ(3);

console.log("\nRysuj litere Z o wysokosci 4");
rysujZ(4);

