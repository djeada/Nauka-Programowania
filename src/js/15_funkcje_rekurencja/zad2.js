/*

Tytuł: Suma liczb naturalnych mniejszych od N.

Treść: Otrzymujesz liczbę N. Przy użyciu rekurencji oblicz sumę liczb naturalnych mniejszych od N.

Dane wejściowe: Liczba naturalna N.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla N = 10, powinna zostać zwrócona liczba: 55.
*/

function sumaLiczbNaturalnych(n) {
  if (n === 0) {
    return 0;
  }
  return n + sumaLiczbNaturalnych(n - 1);
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function test() {
  assert(sumaLiczbNaturalnych(0) === 0, "Test 1 failed");
  assert(sumaLiczbNaturalnych(1) === 1, "Test 2 failed");
  assert(sumaLiczbNaturalnych(2) === 3, "Test 3 failed");
  assert(sumaLiczbNaturalnych(3) === 6, "Test 4 failed");
  assert(sumaLiczbNaturalnych(4) === 10, "Test 5 failed");
  assert(sumaLiczbNaturalnych(5) === 15, "Test 6 failed");
  assert(sumaLiczbNaturalnych(6) === 21, "Test 7 failed");
  assert(sumaLiczbNaturalnych(7) === 28, "Test 8 failed");
  assert(sumaLiczbNaturalnych(8) === 36, "Test 9 failed");
  assert(sumaLiczbNaturalnych(9) === 45, "Test 10 failed");
  assert(sumaLiczbNaturalnych(10) === 55, "Test 11 failed");
}

test();
