/*

Tytuł: Operacje arytmetyczne.

Treść: Otrzymujesz dwie liczby naturalne. Używając jedynie operatorów bitowych, zaimplementuj:

a) Dodawanie.

b) Odejmowanie.

c) Mnożenie.

d) Dzielenie.

Dane wejściowe: Dwie liczby naturalne w każdym podpunkcie.

Dane wyjściowe: Liczba naturalna w każdym podpunkcie.

Przykład:

a) Dla otrzymanych liczb: 2 i 3, powinna zostać zwrócona liczba: 5.

b) Dla otrzymanych liczb: 7 i 5, powinna zostać zwrócona liczba: 2.

c) Dla otrzymanych liczb: 4 i 4, powinna zostać zwrócona liczba: 16.

d) Dla otrzymanych liczb: 9 i 3, powinna zostać zwrócona liczba: 3.
*/

// Dodawanie
function dodaj(a, b) {
  while (b != 0) {
    let carry = a & b;
    a = a ^ b;
    b = carry << 1;
  }
  return a;
}

// Odejmowanie
function odejmij(a, b) {
  while (b != 0) {
    let borrow = ~a & b;
    a = a ^ b;
    b = borrow << 1;
  }
  return a;
}

// Mnożenie
function pomnoz(a, b) {
  let wynik = 0;
  while (b != 0) {
    if (b & 1) {
      wynik = dodaj(wynik, a);
    }
    a <<= 1;
    b >>= 1;
  }
  return wynik;
}

// Testy
function test() {
  let a = 2;
  let b = 3;
  console.assert(dodaj(a, b) === a + b, "Niepoprawny wynik dodawania");
  console.assert(odejmij(a, b) === a - b, "Niepoprawny wynik odejmowania");
  console.assert(pomnoz(a, b) === a * b, "Niepoprawny wynik mnożenia");
}

test();
