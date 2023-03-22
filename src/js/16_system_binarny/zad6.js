/*

Tytuł:  Konwersja między dowolnymi systemami liczbowymi.

Treść: Otrzymujesz liczbę naturalną, podstawę systemu liczbowego, w którym zapisana jest ta liczba, oraz podstawę systemu, na który ma zostać dokonana konwersja. Zwróć reprezentację otrzymanej liczby w nowym systemie.

Dane wejściowe: Trzy liczby naturalne.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanych liczb: 4301, 10 i 4 powinna zostać zwrócona liczba: 1003031.
*/
function konwersjaSystemow(liczba, podstawa1, podstawa2) {
  let dziesietna = 0;
  let reszta = 0;
  let potega = 0;
  let wynik = "";

  // konwersja na system dziesiętny
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
    console.log("Test zakończony sukcesem.");
  } else {
    console.log("Test nie powiódł się.");
  }
}

test();
