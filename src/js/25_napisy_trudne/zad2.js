/*

Tytuł: Usuń podnapis.

Treść: Dostajesz dwa napisy. Twoim zadaniem jest wyszukanie i usunięcie wszystkich wystąpień drugiego napisu w pierwszym napisie.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Napis.

Przykład:

Dla napisów: “Lezy jezy na wiezy” oraz “zy”, zwrócony napis powinien brzmieć: “Le je na wie”.

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
