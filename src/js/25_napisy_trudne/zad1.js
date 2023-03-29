/*

Tytuł: Podmiana słowa w zdaniu.

Treść: Masz trzy napisy: zdanie, słowo A i słowo B. Twoim zadaniem jest zamiana wszystkich wystąpień słowa A na słowo B w zdaniu.

Dane wejściowe: Trzy napisy.

Dane wyjściowe: Napis.

Przykład:

Dla napisów: “Lezy jezy na wiezy”, “zy” oraz “rzy”, zwrócony napis powinien brzmieć: “Lerzy jerzy na wierzy”.

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
