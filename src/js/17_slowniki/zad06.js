/*

Tytul: Histogram wystapien znakow w slowie.

Tresc: Otrzymujesz napis. Znajdz czestosc wystepowania znakow w otrzymanym napisie. Innymi slowy, zwroc histogram znakow w otrzymanym napisie.

Dane wejsciowe: Napis.

Dane wyjsciowe: Slownik par znakow i liczb naturalnych.

Przyklad:

Dla otrzymanego napisu: “klasa”, slownik powinien wygladac nastepujaco: {“k”: 1, “l”: 1, “a”: 2, “s”: 1}.

*/

function histogram(napis) {
  const slownik = {};
  for (let i = 0; i < napis.length; i++) {
    const znak = napis[i];
    if (slownik[znak]) {
      slownik[znak]++;
    } else {
      slownik[znak] = 1;
    }
  }
  return slownik;
}

function testHistogram() {
  const wynik1 = histogram("klasa");
  console.assert(wynik1["k"] === 1, "Test 1 nie powiodl sie");
  console.assert(wynik1["l"] === 1, "Test 2 nie powiodl sie");
  console.assert(wynik1["a"] === 2, "Test 3 nie powiodl sie");
  console.assert(wynik1["s"] === 1, "Test 4 nie powiodl sie");

  const wynik2 = histogram("ala ma kota");
  console.assert(wynik2["a"] === 4, "Test 5 nie powiodl sie");
  console.assert(wynik2["m"] === 2, "Test 6 nie powiodl sie");
}

testHistogram();

