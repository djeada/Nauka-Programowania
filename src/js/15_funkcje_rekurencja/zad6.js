/*

Tytul: N-ty wyraz ciagu danego wzorem rekurencyjnym.

Tresc: Otrzymujesz liczbe N. Oblicz wartosc N-tego wyrazu ciagu danego wzorem rekurencyjnym:

* $a_1 = 1$
* $a_n = 1+2*a_{n-1}$

Dane wejsciowe: Liczba naturalna N.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla N = 5, powinna zostac zwrocona liczba: 31.
*/

function ciag(n) {
  if (n === 1) {
    return 1;
  }
  return 1 + 2 * ciag(n - 1);
}

function test() {
  console.assert(ciag(1) === 1, "Test 1 failed");
  console.assert(ciag(2) === 3, "Test 2 failed");
  console.assert(ciag(3) === 7, "Test 3 failed");
  console.assert(ciag(4) === 15, "Test 4 failed");
  console.assert(ciag(5) === 31, "Test 5 failed");
  console.assert(ciag(6) === 63, "Test 6 failed");
  console.assert(ciag(7) === 127, "Test 7 failed");
  console.assert(ciag(8) === 255, "Test 8 failed");
  console.assert(ciag(9) === 511, "Test 9 failed");
  console.assert(ciag(10) === 1023, "Test 10 failed");
  console.assert(ciag(11) === 2047, "Test 11 failed");
}

test();

