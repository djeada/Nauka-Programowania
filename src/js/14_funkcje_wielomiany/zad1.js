/*
Tytuł: Obliczenie wartości wielomianu w punkcie.

Treść: Otrzymujesz listę n współczynników wielomianu w postaci $a_nx^n + a_{n-1}x^{n-1} + ... + a_0$ oraz liczbę naturalną x. Znajdź wartość wielomianu w podanym punkcie.

Dane wejściowe: Lista liczb naturalnych i liczba naturalna.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla listy współczynników [3, 2, 1] i liczby x = 1, zostanie zwrócona liczba 6.
*/

function wielomian(wspolczynniki, x) {
  let suma = 0;
  for (let i = 0; i < wspolczynniki.length; i++) {
    suma += wspolczynniki[i] * Math.pow(x, i);
  }
  return suma;
}

function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}

function test_wielomian() {
  assert(wielomian([3, 2, 1], 1) === 6, "Błąd testu 1");
  assert(wielomian([3, 2, 1], 2) === 17, "Błąd testu 2");
  assert(wielomian([3, 2, 1], 3) === 36, "Błąd testu 3");
  assert(wielomian([3, 2, 1], 4) === 63, "Błąd testu 4");
  assert(wielomian([3, 2, 1], 5) === 98, "Błąd testu 5");
  assert(wielomian([3, 2, 1], 6) === 141, "Błąd testu 6");
  assert(wielomian([3, 2, 1], 7) === 192, "Błąd testu 7");
  assert(wielomian([3, 2, 1], 8) === 251, "Błąd testu 8");
  assert(wielomian([3, 2, 1], 9) === 318, "Błąd testu 9");
  assert(wielomian([3, 2, 1], 10) === 393, "Błąd testu 10");
}

test_wielomian();
