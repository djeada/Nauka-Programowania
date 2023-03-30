/*
Tytul: Liczby naturalne mniejsze od N.

Tresc: Otrzymujesz liczbe N. Przy uzyciu rekurencji stworz napis skladajacy sie z liczb naturalnych mniejszych od N oddzielonych przecinkami.

Dane wejsciowe: Liczba naturalna N.

Dane wyjsciowe: Napis.

Przyklad:

Dla N = 10, powinien zostac zwrocony napis: "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0".
*/

function liczbyMniejszeOdN(n) {
  if (n === 0) {
    return "0";
  }
  return n + ", " + liczbyMniejszeOdN(n - 1);
}

// Testy

function test() {
  const n = 10;
  const wynik = "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0";
  console.assert(
    liczbyMniejszeOdN(n) === wynik,
    `Niepoprawny wynik dla liczby ${n}.`
  );
}

test();

