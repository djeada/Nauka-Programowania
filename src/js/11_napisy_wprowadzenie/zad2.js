/*
Tytuł: Policz wystąpienia znaku.

Treść: Dla podanego napisu i znaku, znajdź liczbę wystąpień tego znaku w napisie.

Dane wejściowe: Napis oraz znak.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanego napisu: "klamra" oraz znaku 'a', powinno zostać zwrócone: 2.
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

  console.assert(output === expectedOutput, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");
}

test();
