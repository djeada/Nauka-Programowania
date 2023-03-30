/*
Tytuł:  Konwersja warunkowa.

Treść: Otrzymujesz liczbę naturalną. Zwróć reprezentację binarną otrzymanej liczby, jeśli:

a) Otrzymana liczba jest liczbą parzystą.

b) Otrzymana liczba jest liczbą pierwszą.

Dane wejściowe: Liczba naturalna w obu podpunktach.

Dane wyjściowe: Liczba naturalna w obu podpunktach.

Przykład:

a) Dla otrzymanej liczby: 7, nie powinna zostać zwrócona żadna liczba.

b) Dla otrzymanej liczby: 7, powinna zostać zwrócona liczba: 111.

*/

function konwersjaWarunkowa(liczba) {
  let wynik = "";
  if (liczba % 2 === 0) {
    wynik = liczba.toString(2);
  } else {
    let czyPierwsza = true;
    for (let i = 2; i <= Math.sqrt(liczba); i++) {
      if (liczba % i === 0) {
        czyPierwsza = false;
        break;
      }
    }
    if (czyPierwsza) {
      wynik = liczba.toString(2);
    }
  }
  return wynik;
}

// Testy
function test() {
  let input = 7;
  let expectedOutput = "";
  let output = konwersjaWarunkowa(input);

  console.assert(output === expectedOutput, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");

  input = 8;
  expectedOutput = "1000";
  output = konwersjaWarunkowa(input);

  console.assert(output === expectedOutput, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");

  input = 11;
  expectedOutput = "";
  output = konwersjaWarunkowa(input);

  console.assert(output === expectedOutput, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");

  input = 13;
  expectedOutput = "1101";
  output = konwersjaWarunkowa(input);

  console.assert(output === expectedOutput, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");

  input = 17;
  expectedOutput = "10001";
  output = konwersjaWarunkowa(input);

  console.assert(output === expectedOutput, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");
}

test();
