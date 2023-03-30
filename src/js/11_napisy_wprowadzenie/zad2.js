/*
Tytul: Policz wystapienia znaku.

Tresc: Dla podanego napisu i znaku, znajdz liczbe wystapien tego znaku w napisie.

Dane wejsciowe: Napis oraz znak.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanego napisu: "klamra" oraz znaku 'a', powinno zostac zwrocone: 2.
*/
function policzWystapieniaZnaku(napis, znak) {
  let licznik = 0;
  for (let i = 0; i < napis.length; i++) {
    if (napis[i] === znak) {
      licznik++;
    }
  }
  return licznik;
}

// Testy

function test() {
  let input1 = "klamra";
  let input2 = "a";
  let expectedOutput = 2;
  let output = policzWystapieniaZnaku(input1, input2);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

