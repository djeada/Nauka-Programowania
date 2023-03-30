/*

Tytul: Czy napis sklada sie wylacznie z cyfr?

Tresc: Masz napis. Sprawdz, czy sklada sie on wylacznie z cyfr.

Dane wejsciowe: Napis.

Dane wyjsciowe: Wartosc logiczna.

Przyklad:

Dla napisu: “1234”, powinna zostac zwrocona wartosc logiczna: Prawda.

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

