/*
Tytuł: Silnia.

Treść: Napisz funkcję, która obliczy silnię otrzymanej liczby naturalnej, przy pomocy pętli.

Dane wejściowe: liczba naturalna

Dane wyjściowe: liczba naturalna

Przykład:

Dla otrzymanej liczby 3, funkcja powinna zwrócić liczbę 6.
*/

// Funkcja zwracająca silnię liczby
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

// Funkcja uruchamiająca testy
function main() {
  testSilnia();
}

// Uruchomienie testów
main();
