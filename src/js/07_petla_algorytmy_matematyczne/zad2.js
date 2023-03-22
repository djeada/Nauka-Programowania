/*
Tytuł: Podnieś a do b.	

Treść: Napisz funkcję, która dla otrzymanych dwóch liczb obliczy ile wynosi a podniesione do b, przy pomocy pętli.

Dane wejściowe: dwie liczby naturalne

Dane wyjściowe: liczba naturalna

Przykład:

Dla pobranych liczb 3 i 5, funkcja powinna zwrócić liczbę 243.
*/

// Funkcja zwracająca a podniesione do b
function podniesDoPotegi(a, b) {
  var wynik = 1;
  for (var i = 0; i < b; i++) {
    wynik *= a;
  }
  return wynik;
}

// Testy
function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
}

function testPotega() {
  assert(podniesDoPotegi(2, 3) == 8);
  assert(podniesDoPotegi(3, 2) == 9);
  assert(podniesDoPotegi(4, 4) == 256);
  assert(podniesDoPotegi(5, 3) == 125);
  assert(podniesDoPotegi(6, 0) == 1);
  assert(podniesDoPotegi(7, 1) == 7);
  assert(podniesDoPotegi(0, 2) == 0);
}

// Funkcja uruchamiająca testy
function main() {
  testPotega();
}

// Uruchomienie testów
main();
