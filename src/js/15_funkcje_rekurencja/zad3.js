/*

Tytuł: Potęga.

Treść: Otrzymujesz dwie liczby, a i b. Przy użyciu rekurencji oblicz a podniesione do b.

Dane wejściowe: Dwie liczby naturalne a i b.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla a = 2 i b = 3, powinna zostać zwrócona liczba: 8.
*/

function potega(a, b) {
  if (b === 0) {
    return 1;
  }
  return a * potega(a, b - 1);
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function test() {
  assert(potega(2, 0) === 1, "Test 1 failed");
  assert(potega(2, 1) === 2, "Test 2 failed");
  assert(potega(2, 2) === 4, "Test 3 failed");
  assert(potega(2, 3) === 8, "Test 4 failed");
  assert(potega(2, 4) === 16, "Test 5 failed");
  assert(potega(2, 5) === 32, "Test 6 failed");
  assert(potega(2, 6) === 64, "Test 7 failed");
  assert(potega(2, 7) === 128, "Test 8 failed");
  assert(potega(2, 8) === 256, "Test 9 failed");
  assert(potega(2, 9) === 512, "Test 10 failed");
  assert(potega(2, 10) === 1024, "Test 11 failed");
}

test();
