/*

Tytul:  Konwersja miedzy dowolnymi systemami liczbowymi.

Tresc: Otrzymujesz liczbe naturalna, podstawe systemu liczbowego, w ktorym zapisana jest ta liczba, oraz podstawe systemu, na ktory ma zostac dokonana konwersja. Zwroc reprezentacje otrzymanej liczby w nowym systemie.

Dane wejsciowe: Trzy liczby naturalne.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanych liczb: 4301, 10 i 4 powinna zostac zwrocona liczba: 1003031.
*/
function konwersjaSystemow(liczba, podstawa1, podstawa2) {
  let dziesietna = 0;
  let reszta = 0;
  let potega = 0;
  let wynik = "";

  // konwersja na system dziesietny
  while (liczba > 0) {
    reszta = liczba % 10;
    dziesietna += reszta * Math.pow(podstawa1, potega);
    potega++;
    liczba = Math.floor(liczba / 10);
  }

  // konwersja na nowy system
  while (dziesietna > 0) {
    reszta = dziesietna % podstawa2;
    wynik = reszta + wynik;
    dziesietna = Math.floor(dziesietna / podstawa2);
  }

  return wynik ? wynik : "0";
}

// testy
function test() {
  const liczba1 = 4301;
  const podstawa1 = 10;
  const podstawa2 = 4;
  const wynik = "1003031";

  if (konwersjaSystemow(liczba1, podstawa1, podstawa2) === wynik) {
    console.log("Test zakonczony sukcesem.");
  } else {
    console.log("Test nie powiodl sie.");
  }
}

test();

