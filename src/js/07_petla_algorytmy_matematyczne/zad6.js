/*
Tytuł: NWW.

Treść: Napisz funkcję, która dla otrzymanych dwóch liczb naturalnych zwróci ich najmniejszą wspólną wielokrotność.

Dane wejściowe: dwie liczby naturalne

Dane wyjściowe: liczba naturalna

Przykład:

Dla otrzymanych liczb 7 i 9, funkcja powinna zwrócić liczbę 63.
*/

// Funkcja zwracająca NWW
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

// Funkcja uruchamiająca testy
function main() {
  testNWW();
}

// Uruchomienie testów
main();
