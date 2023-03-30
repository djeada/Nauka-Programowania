/*
Tytul: Choinka.

Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej N, wypisze N trojkatow ustawionych w kolumnie, jeden na drugim. Wysokosc pierwszego trojkata to 1, a kazdego nastepnego jest rowna wysokosci poprzedniego powiekszonej o 1.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Komunikat.

Przyklad:

Dla otrzymanej liczby 3 powinno zostac wypisane:

    *
    *
    **
    *
    **
    ***
    */

// Funkcja wypisujaca N trojkatow ustawionych w kolumnie
function rysujChoinke(n) {
  var wiersz = "";
  for (var i = 0; i < n; i++) {
    for (var j = 0; j <= i; j++) {
      wiersz += "*";
      console.log(wiersz);
    }
    wiersz = "";
  }
}

// Testy
console.log("Rysuj choinke o wysokosci 2");
rysujChoinke(2);

console.log("\nRysuj choinke o wysokosci 3");
rysujChoinke(3);

console.log("\nRysuj choinke o wysokosci 4");
rysujChoinke(4);

