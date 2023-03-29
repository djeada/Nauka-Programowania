/*

Tytuł: Usuń powtórzenia znaków.

Treść: Otrzymujesz napis. Twoim zadaniem jest usunięcie powtórzeń każdego znaku w napisie. Każdy znak może wystąpić tylko raz.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla napisu: “AAAAAAAAAABBBBBBBBA”, zwrócony napis powinien brzmieć: “AB”.

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
