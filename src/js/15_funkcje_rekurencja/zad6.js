/*

Tytuł: N-ty wyraz ciągu danego wzorem rekurencyjnym.

Treść: Otrzymujesz liczbę N. Oblicz wartość N-tego wyrazu ciągu danego wzorem rekurencyjnym:

* $a_1 = 1$
* $a_n = 1+2*a_{n-1}$

Dane wejściowe: Liczba naturalna N.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla N = 5, powinna zostać zwrócona liczba: 31.
*/

function ciag(n) {
  if (n === 1) {
    return 1;
  }
  return 1 + 2 * ciag(n - 1);
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function test() {
  assert(ciag(1) === 1, "Test 1 failed");
  assert(ciag(2) === 3, "Test 2 failed");
  assert(ciag(3) === 7, "Test 3 failed");
  assert(ciag(4) === 15, "Test 4 failed");
  assert(ciag(5) === 31, "Test 5 failed");
  assert(ciag(6) === 63, "Test 6 failed");
  assert(ciag(7) === 127, "Test 7 failed");
  assert(ciag(8) === 255, "Test 8 failed");
  assert(ciag(9) === 511, "Test 9 failed");
  assert(ciag(10) === 1023, "Test 10 failed");
  assert(ciag(11) === 2047, "Test 11 failed");
}

test();
