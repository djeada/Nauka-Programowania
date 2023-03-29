/*

Tytuł: Usuń powtórzenia stojących obok siebie znaków.

Treść: Otrzymujesz napis. Twoim zadaniem jest usunięcie powtórzeń stojących obok siebie znaków i zachowanie tylko pierwszego wystąpienia każdego znaku.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla napisu: “AAAAAAAAAABBBBBBBBA”, zwrócony napis powinien brzmieć: “ABA”.

*/

function usunSasiedniePowtorzenia(napis) {
  let wynik = "";
  for (let i = 0; i < napis.length; i++) {
    if (napis[i] !== napis[i + 1]) {
      wynik += napis[i];
    }
  }
  return wynik;
}

function testUsunSasiedniePowtorzenia() {
  const napis = "AAAAAAAAAABBBBBBBBA";
  const wynik = "ABA";
  console.assert(usunSasiedniePowtorzenia(napis) === wynik, "Test nieudany");
}

testUsunSasiedniePowtorzenia();
