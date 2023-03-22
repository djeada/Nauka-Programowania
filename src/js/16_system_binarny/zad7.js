/*

Tytuł: Odwrócenie sąsiadujących bitów.

Treść: Otrzymujesz reprezentację dziesiętną liczby naturalnej. Zmień miejscami sąsiadujące bity w zapisie binarnym tej liczby i zwróć dziesiętną reprezentację wyniku.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej liczby: 9131, powinna zostać zwrócona liczba: 4951.

*/

function odwrocSasiadujaceBity(liczba) {
  let binary = (liczba >>> 0).toString(2); // konwersja na system binarny
  let n = binary.length;
  let wynik = "";

  for (let i = 0; i < n; i += 2) {
    // zamiana sąsiadujących bitów
    if (i == n - 1) {
      // dodanie ostatniego bitu, jeśli długość binarna jest nieparzysta
      wynik += binary[i];
    } else {
      wynik += binary[i + 1] + binary[i];
    }
  }

  return parseInt(wynik, 2); // konwersja na system dziesiętny
}

// test
function test() {
  let input = 9131;
  let expectedOutput = 4951;
  let output = odwrocSasiadujaceBity(input);

  assert(output === expectedOutput, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");
}

function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}

test();
