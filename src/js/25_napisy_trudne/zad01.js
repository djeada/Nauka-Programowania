/*

Tytul: Podmiana slowa w zdaniu.

Tresc: Masz trzy napisy: zdanie, slowo A i slowo B. Twoim zadaniem jest zamiana wszystkich wystapien slowa A na slowo B w zdaniu.

Dane wejsciowe: Trzy napisy.

Dane wyjsciowe: Napis.

Przyklad:

Dla napisow: “Lezy jezy na wiezy”, “zy” oraz “rzy”, zwrocony napis powinien brzmiec: “Lerzy jerzy na wierzy”.

*/

function podmianaSlowa(zdanie, slowoA, slowoB) {
  return zdanie.split(slowoA).join(slowoB);
}

function testPodmianaSlowa() {
  const zdanie = "Lezy jezy na wiezy";
  const slowoA = "zy";
  const slowoB = "rzy";
  const wynik = "Lerzy jerzy na wierzy";
  console.assert(
    podmianaSlowa(zdanie, slowoA, slowoB) === wynik,
    "Test nieudany"
  );
}

testPodmianaSlowa();

