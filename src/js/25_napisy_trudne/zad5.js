/*

Tytul: Usun powtorzenia stojacych obok siebie znakow.

Tresc: Otrzymujesz napis. Twoim zadaniem jest usuniecie powtorzen stojacych obok siebie znakow i zachowanie tylko pierwszego wystapienia kazdego znaku.

Dane wejsciowe: Napis.

Dane wyjsciowe: Napis.

Przyklad:

Dla napisu: “AAAAAAAAAABBBBBBBBA”, zwrocony napis powinien brzmiec: “ABA”.

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

