/*
Tytuł: NWD.

Treść: Napisz funkcję, która dla otrzymanych dwóch liczb naturalnych zwróci ich największy wspólny dzielnik.

Dane wejściowe: dwie liczby naturalne

Dane wyjściowe: liczba naturalna

Przykład:

Dla otrzymanych liczb 60 i 45, funkcja powinna zwrócić liczbę 15.
*/

// Funkcja zwracająca NWD
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
function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
}

function testNWD() {
  assert(zwracajNWD(2, 3) == 1);
  assert(zwracajNWD(3, 2) == 1);
  assert(zwracajNWD(4, 4) == 4);
  assert(zwracajNWD(5, 3) == 1);
  assert(zwracajNWD(6, 0) == 6);
  assert(zwracajNWD(7, 1) == 1);
  assert(zwracajNWD(0, 2) == 2);
}

// Funkcja uruchamiająca testy
function main() {
  testNWD();
}

// Uruchomienie testów
main();
