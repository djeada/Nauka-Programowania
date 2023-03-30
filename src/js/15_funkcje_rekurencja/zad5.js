/*
Tytuł: Liczba Fibonacciego.

Treść: Otrzymujesz liczbę N. Przy użyciu rekurencji oblicz wartość N-tego wyrazu ciągu Fibonacciego.

Podpowiedź: Ciąg Fibonacciego zdefiniowany jest następująco:

* $a_0= 0$,
* $a_1= 1$,
* $a_n= a_{n-1}+a_n-2$.

Dane wejściowe: Liczba naturalna N.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla N = 7, powinna zostać zwrócona liczba: 13.
*/

function fib(n) {
  if (n === 0) {
    return 0;
  }
  if (n === 1) {
    return 1;
  }
  return fib(n - 1) + fib(n - 2);
}

function test() {
  console.assert(fib(0) === 0, "Test 1 failed");
  console.assert(fib(1) === 1, "Test 2 failed");
  console.assert(fib(2) === 1, "Test 3 failed");
  console.assert(fib(3) === 2, "Test 4 failed");
  console.assert(fib(4) === 3, "Test 5 failed");
  console.assert(fib(5) === 5, "Test 6 failed");
  console.assert(fib(6) === 8, "Test 7 failed");
  console.assert(fib(7) === 13, "Test 8 failed");
  console.assert(fib(8) === 21, "Test 9 failed");
  console.assert(fib(9) === 34, "Test 10 failed");
  console.assert(fib(10) === 55, "Test 11 failed");
}

test();
