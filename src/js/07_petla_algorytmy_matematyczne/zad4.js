/*
Tytul: Silnia.

Tresc: Napisz funkcje, ktora obliczy silnie otrzymanej liczby naturalnej, przy pomocy petli.

Dane wejsciowe: liczba naturalna

Dane wyjsciowe: liczba naturalna

Przyklad:

Dla otrzymanej liczby 3, funkcja powinna zwrocic liczbe 6.
*/

// Funkcja zwracajaca silnie liczby
function silnia(liczba) {
  var wynik = 1;
  for (var i = 1; i <= liczba; i++) {
    wynik *= i;
  }
  return wynik;
}

// Testy

function testSilnia() {
  console.assert(silnia(2) == 2);
  console.assert(silnia(3) == 6);
  console.assert(silnia(4) == 24);
  console.assert(silnia(5) == 120);
  console.assert(silnia(6) == 720);
  console.assert(silnia(7) == 5040);
  console.assert(silnia(8) == 40320);
}

// Funkcja uruchamiajaca testy
function main() {
  testSilnia();
}

// Uruchomienie testow
main();

