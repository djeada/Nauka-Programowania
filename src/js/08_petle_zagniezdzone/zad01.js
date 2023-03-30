/*
Tytul: Kwadrat

Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej wypisze kwadrat o boku rownym tej liczbie.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Komunikat.

Przyklad:

Dla otrzymanej liczby 2 powinno zostac wypisane:

    **
    **
*/

// Funkcja wypisujaca kwadrat o boku rownym liczbie
function rysujKwadrat(bok) {
  var wiersz = "";
  for (var i = 0; i < bok; i++) {
    wiersz += "*";
  }

  for (var j = 0; j < bok; j++) {
    console.log(wiersz);
  }
}

// Testy
console.log("Rysuj kwadrat o boku 2");
rysujKwadrat(2);

console.log("\nRysuj kwadrat o boku 3");
rysujKwadrat(3);

console.log("\nRysuj kwadrat o boku 4");
rysujKwadrat(4);

