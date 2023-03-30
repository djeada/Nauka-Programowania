/*
Tytul: Z ilu slow sklada sie zdanie?

Tresc: Zlicz, ile slow sklada sie z podanego zdania. Znaki interpunkcyjne nie sa brane pod uwage jako slowa.

Dane wejsciowe: Napis.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanego napisu: "gram na pianinie.", powinno zostac zwrocone: 3.
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

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

