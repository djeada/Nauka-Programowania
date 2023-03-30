/*
Tytul: Tabliczka mnozenia.

Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej N, wypisze N pierwszych wierszy i kolumn tabliczki mnozenia.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Wiersze i kolumny tabliczki mnozenia o wymiarach NxN.

Przyklad:

Dla otrzymanej liczby 3 powinno zostac wypisane:

    1 2 3
    2 4 6
    3 6 9

    */

// Funkcja wypisujaca tabliczke mnozenia o wymiarach NxN
function tabliczkaMnozenia(n) {
  for (var i = 1; i <= n; i++) {
    var wiersz = "";
    for (var j = 1; j <= n; j++) {
      wiersz += i * j + " ";
    }
    console.log(wiersz);
  }
}

// Testy
console.log("Tabliczka mnozenia o wymiarach 2x2");
tabliczkaMnozenia(2);

console.log("\nTabliczka mnozenia o wymiarach 3x3");
tabliczkaMnozenia(3);

console.log("\nTabliczka mnozenia o wymiarach 4x4");
tabliczkaMnozenia(4);

