/*

Tytul: Trojkat Pascala.

Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze trojkat Pascala o wysokosci rownej tej liczbie.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Komunikat.

Przyklad:

Dla otrzymanej liczby 3 powinno zostac wypisane:

  1
  11
  121

*/

// Funkcja wypisujaca trojkat Pascala o wysokosci rownej liczbie
function rysujTrojkatPascala(wysokosc) {
  var trojkat = [];

  for (var i = 0; i < wysokosc; i++) {
    trojkat[i] = new Array(i + 1);

    for (var j = 0; j <= i; j++) {
      if (j == 0 || j == i) {
        trojkat[i][j] = 1;
      } else {
        trojkat[i][j] = trojkat[i - 1][j - 1] + trojkat[i - 1][j];
      }
    }
  }

  for (i = 0; i < wysokosc; i++) {
    var wiersz = "";
    for (j = 0; j <= i; j++) {
      wiersz += trojkat[i][j] + " ";
    }
    console.log(wiersz);
  }
}

// Testy
console.log("Rysuj trojkat Pascala o wysokosci 2");
rysujTrojkatPascala(2);

console.log("\nRysuj trojkat Pascala o wysokosci 3");
rysujTrojkatPascala(3);

console.log("\nRysuj trojkat Pascala o wysokosci 4");
rysujTrojkatPascala(4);

