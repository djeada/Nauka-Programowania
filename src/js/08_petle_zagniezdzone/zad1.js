/*
Tytuł: Kwadrat

Treść: Napisz funkcję, która dla otrzymanej liczby naturalnej wypisze kwadrat o boku równym tej liczbie.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Komunikat.

Przykład:

Dla otrzymanej liczby 2 powinno zostać wypisane:

    **
    **
*/

// Funkcja wypisująca kwadrat o boku równym liczbie
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
