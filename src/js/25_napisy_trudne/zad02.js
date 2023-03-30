/*

Tytul: Usun podnapis.

Tresc: Dostajesz dwa napisy. Twoim zadaniem jest wyszukanie i usuniecie wszystkich wystapien drugiego napisu w pierwszym napisie.

Dane wejsciowe: Dwa napisy.

Dane wyjsciowe: Napis.

Przyklad:

Dla napisow: “Lezy jezy na wiezy” oraz “zy”, zwrocony napis powinien brzmiec: “Le je na wie”.

*/

function usunPodnapis(napis, podnapis) {
  return napis.split(podnapis).join("");
}

function testUsunPodnapis() {
  const napis = "Lezy jezy na wiezy";
  const podnapis = "zy";
  const wynik = "Le je na wie";
  console.assert(usunPodnapis(napis, podnapis) === wynik, "Test nieudany");
}

testUsunPodnapis();

