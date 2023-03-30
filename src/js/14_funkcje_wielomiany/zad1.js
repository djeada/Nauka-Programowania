/*
Tytul: Obliczenie wartosci wielomianu w punkcie.

Tresc: Otrzymujesz liste n wspolczynnikow wielomianu w postaci $a_nx^n + a_{n-1}x^{n-1} + ... + a_0$ oraz liczbe naturalna x. Znajdz wartosc wielomianu w podanym punkcie.

Dane wejsciowe: Lista liczb naturalnych i liczba naturalna.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla listy wspolczynnikow [3, 2, 1] i liczby x = 1, zostanie zwrocona liczba 6.
*/

function wielomian(wspolczynniki, x) {
  let suma = 0;
  for (let i = 0; i < wspolczynniki.length; i++) {
    suma += wspolczynniki[i] * Math.pow(x, i);
  }
  return suma;
}

function test_wielomian() {
  console.assert(wielomian([3, 2, 1], 1) === 6, "Blad testu 1");
  console.assert(wielomian([3, 2, 1], 2) === 17, "Blad testu 2");
  console.assert(wielomian([3, 2, 1], 3) === 36, "Blad testu 3");
  console.assert(wielomian([3, 2, 1], 4) === 63, "Blad testu 4");
  console.assert(wielomian([3, 2, 1], 5) === 98, "Blad testu 5");
  console.assert(wielomian([3, 2, 1], 6) === 141, "Blad testu 6");
  console.assert(wielomian([3, 2, 1], 7) === 192, "Blad testu 7");
  console.assert(wielomian([3, 2, 1], 8) === 251, "Blad testu 8");
  console.assert(wielomian([3, 2, 1], 9) === 318, "Blad testu 9");
  console.assert(wielomian([3, 2, 1], 10) === 393, "Blad testu 10");
}

test_wielomian();

