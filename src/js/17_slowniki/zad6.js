/*

Tytuł: Histogram wystąpień znaków w słowie.

Treść: Otrzymujesz napis. Znajdź częstość występowania znaków w otrzymanym napisie. Innymi słowy, zwróć histogram znaków w otrzymanym napisie.

Dane wejściowe: Napis.

Dane wyjściowe: Słownik par znaków i liczb naturalnych.

Przykład:

Dla otrzymanego napisu: “klasa”, słownik powinien wyglądać następująco: {“k”: 1, “l”: 1, “a”: 2, “s”: 1}.

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
  assert(wynik1["k"] === 1, "Test 1 nie powiódł się");
  assert(wynik1["l"] === 1, "Test 2 nie powiódł się");
  assert(wynik1["a"] === 2, "Test 3 nie powiódł się");
  assert(wynik1["s"] === 1, "Test 4 nie powiódł się");

  const wynik2 = histogram("ala ma kota");
  assert(wynik2["a"] === 4, "Test 5 nie powiódł się");
  assert(wynik2["m"] === 2, "Test 6 nie powiódł się");
}

// test
function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Asercja nie powiodła się");
  }
}

testHistogram();
