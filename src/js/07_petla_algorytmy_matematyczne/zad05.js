/*
Tytul: NWD.

Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb naturalnych zwroci ich najwiekszy wspolny dzielnik.

Dane wejsciowe: dwie liczby naturalne

Dane wyjsciowe: liczba naturalna

Przyklad:

Dla otrzymanych liczb 60 i 45, funkcja powinna zwrocic liczbe 15.
*/

// Funkcja zwracajaca NWD
function zwracajNWD(liczba_a, liczba_b) {
  var dzielnik = 1;
  for (var i = 1; i <= liczba_a; i++) {
    if (liczba_a % i == 0 && liczba_b % i == 0) {
      dzielnik = i;
    }
  }
  return dzielnik;
}

// Testy

function testNWD() {
  console.assert(zwracajNWD(2, 3) == 1);
  console.assert(zwracajNWD(3, 2) == 1);
  console.assert(zwracajNWD(4, 4) == 4);
  console.assert(zwracajNWD(5, 3) == 1);
  console.assert(zwracajNWD(6, 0) == 6);
  console.assert(zwracajNWD(7, 1) == 1);
  console.assert(zwracajNWD(0, 2) == 2);
}

// Funkcja uruchamiajaca testy
function main() {
  testNWD();
}

// Uruchomienie testow
main();

