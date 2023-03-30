/*
Tytul: NWW.

Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb naturalnych zwroci ich najmniejsza wspolna wielokrotnosc.

Dane wejsciowe: dwie liczby naturalne

Dane wyjsciowe: liczba naturalna

Przyklad:

Dla otrzymanych liczb 7 i 9, funkcja powinna zwrocic liczbe 63.
*/

// Funkcja zwracajaca NWW
function zwracajNWW(liczba_a, liczba_b) {
  var nww = 1;
  var i = 1;
  while (nww == 1) {
    if (i % liczba_a == 0 && i % liczba_b == 0) {
      nww = i;
    }
    i++;
  }
  return nww;
}

// Testy

function testNWW() {
  console.assert(zwracajNWW(2, 3) == 6);
  console.assert(zwracajNWW(3, 2) == 6);
  console.assert(zwracajNWW(4, 4) == 4);
  console.assert(zwracajNWW(5, 3) == 15);
  console.assert(zwracajNWW(6, 0) == 0);
  console.assert(zwracajNWW(7, 1) == 7);
  console.assert(zwracajNWW(0, 2) == 0);
}

// Funkcja uruchamiajaca testy
function main() {
  testNWW();
}

// Uruchomienie testow
main();

