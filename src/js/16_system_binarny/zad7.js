/*

Tytul: Odwrocenie sasiadujacych bitow.

Tresc: Otrzymujesz reprezentacje dziesietna liczby naturalnej. Zmien miejscami sasiadujace bity w zapisie binarnym tej liczby i zwroc dziesietna reprezentacje wyniku.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanej liczby: 9131, powinna zostac zwrocona liczba: 4951.

*/

function odwrocSasiadujaceBity(liczba) {
  let binary = (liczba >>> 0).toString(2); // konwersja na system binarny
  let n = binary.length;
  let wynik = "";

  for (let i = 0; i < n; i += 2) {
    // zamiana sasiadujacych bitow
    if (i == n - 1) {
      // dodanie ostatniego bitu, jesli dlugosc binarna jest nieparzysta
      wynik += binary[i];
    } else {
      wynik += binary[i + 1] + binary[i];
    }
  }

  return parseInt(wynik, 2); // konwersja na system dziesietny
}

// test
function test() {
  let input = 9131;
  let expectedOutput = 4951;
  let output = odwrocSasiadujaceBity(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

