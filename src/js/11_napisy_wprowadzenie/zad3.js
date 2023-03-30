/*
Tytuł: Z ilu słów składa się zdanie?

Treść: Zlicz, ile słów składa się z podanego zdania. Znaki interpunkcyjne nie są brane pod uwagę jako słowa.

Dane wejściowe: Napis.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanego napisu: "gram na pianinie.", powinno zostać zwrócone: 3.
*/
function policzSlowa(zdanie) {
  let slowa = zdanie.split(" ");
  let liczbaSlow = 0;
  for (let i = 0; i < slowa.length; i++) {
    let slowo = slowa[i].replace(/[.,/#!$%&;:{}=\-_`~()]/g, "");
    if (slowo.length > 0) {
      liczbaSlow++;
    }
  }
  return liczbaSlow;
}

// Testy

function test() {
  let input = "gram na pianinie.";
  let expectedOutput = 3;
  let output = policzSlowa(input);

  console.assert(output === expectedOutput, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");
}

test();
