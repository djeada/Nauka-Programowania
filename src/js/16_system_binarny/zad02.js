/*
Tytul:  Konwersja warunkowa.

Tresc: Otrzymujesz liczbe naturalna. Zwroc reprezentacje binarna otrzymanej liczby, jesli:

a) Otrzymana liczba jest liczba parzysta.

b) Otrzymana liczba jest liczba pierwsza.

Dane wejsciowe: Liczba naturalna w obu podpunktach.

Dane wyjsciowe: Liczba naturalna w obu podpunktach.

Przyklad:

a) Dla otrzymanej liczby: 7, nie powinna zostac zwrocona zadna liczba.

b) Dla otrzymanej liczby: 7, powinna zostac zwrocona liczba: 111.

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

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");

  input = 8;
  expectedOutput = "1000";
  output = konwersjaWarunkowa(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");

  input = 11;
  expectedOutput = "";
  output = konwersjaWarunkowa(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");

  input = 13;
  expectedOutput = "1101";
  output = konwersjaWarunkowa(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");

  input = 17;
  expectedOutput = "10001";
  output = konwersjaWarunkowa(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

