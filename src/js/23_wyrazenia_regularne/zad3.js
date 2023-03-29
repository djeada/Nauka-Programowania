/*

Tytuł: Czy napis składa się wyłącznie z cyfr?

Treść: Masz napis. Sprawdź, czy składa się on wyłącznie z cyfr.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla napisu: “1234”, powinna zostać zwrócona wartość logiczna: Prawda.

*/

function czy_tylko_cyfry(napis) {
  const cyfry = /^[0-9]+$/;

  return cyfry.test(napis);
}

function test_czy_tylko_cyfry() {
  console.assert(czy_tylko_cyfry("1234") === true);
  console.assert(czy_tylko_cyfry("1234a") === false);
  console.assert(czy_tylko_cyfry("a1234") === false);
  console.assert(czy_tylko_cyfry("1234 ") === false);
  console.assert(czy_tylko_cyfry(" 1234") === false);
  console.assert(czy_tylko_cyfry(" 1234 ") === false);
  console.assert(czy_tylko_cyfry("1234.5") === false);
  console.assert(czy_tylko_cyfry("1234,5") === false);
}
test_czy_tylko_cyfry();
