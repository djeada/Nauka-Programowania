/*

Tytuł: Silnia.

Treść: Otrzymujesz liczbę N. Przy użyciu rekurencji oblicz silnię z tej liczby.

Dane wejściowe: Liczba naturalna N.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla N = 3, powinna zostać zwrócona liczba: 6.
*/

function silnia(n) {
  if (n === 0) {
    return 1;
  }
  return n * silnia(n - 1);
}

function test() {
  console.assert(silnia(0) === 1, "Test 1 failed");
  console.assert(silnia(1) === 1, "Test 2 failed");
  console.assert(silnia(2) === 2, "Test 3 failed");
  console.assert(silnia(3) === 6, "Test 4 failed");
  console.assert(silnia(4) === 24, "Test 5 failed");
  console.assert(silnia(5) === 120, "Test 6 failed");
  console.assert(silnia(6) === 720, "Test 7 failed");
  console.assert(silnia(7) === 5040, "Test 8 failed");
  console.assert(silnia(8) === 40320, "Test 9 failed");
  console.assert(silnia(9) === 362880, "Test 10 failed");
  console.assert(silnia(10) === 3628800, "Test 11 failed");
}

test();
