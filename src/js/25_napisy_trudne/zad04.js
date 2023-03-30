/*

Tytul: Usun powtorzenia znakow.

Tresc: Otrzymujesz napis. Twoim zadaniem jest usuniecie powtorzen kazdego znaku w napisie. Kazdy znak moze wystapic tylko raz.

Dane wejsciowe: Napis.

Dane wyjsciowe: Napis.

Przyklad:

Dla napisu: “AAAAAAAAAABBBBBBBBA”, zwrocony napis powinien brzmiec: “AB”.

*/

function usunPowtorzenia(napis) {
  const unikalneZnaki = new Set(napis);
  return Array.from(unikalneZnaki).join("");
}

function testUsunPowtorzenia() {
  const napis = "AAAAAAAAAABBBBBBBBA";
  const wynik = "AB";
  console.assert(usunPowtorzenia(napis) === wynik, "Test nieudany");
}

testUsunPowtorzenia();

