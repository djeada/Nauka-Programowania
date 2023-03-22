/*
Tytuł: Konwersja pomiędzy systemami binarnym i dziesiętnym.

Treść:

a) Otrzymujesz reprezentację dziesiętną liczby naturalnej, zwróć jej reprezentację binarną.

b) Otrzymujesz reprezentację binarną liczby naturalnej, zwróć jej reprezentację dziesiętną.

Dane wejściowe: Liczba naturalna w obu podpunktach.

Dane wyjściowe: Liczba naturalna w obu podpunktach.

Przykład:

a) Dla otrzymanej liczby: 3, powinna zostać zwrócona liczba: 11.

b) Dla otrzymanej liczby: 101, powinna zostać zwrócona liczba: 5.
*/

// a) Konwersja liczby dziesiętnej na binarną
function dziesietnaNaBinarna(dziesietna) {
  let binarna = "";
  while (dziesietna > 0) {
    binarna = (dziesietna % 2) + binarna;
    dziesietna = Math.floor(dziesietna / 2);
  }
  return binarna === "" ? "0" : binarna;
}

// b) Konwersja liczby binarnej na dziesiętną
function binarnaNaDziesietna(binarna) {
  let dziesietna = 0;
  for (let i = 0; i < binarna.length; i++) {
    dziesietna += parseInt(binarna[i]) * Math.pow(2, binarna.length - i - 1);
  }
  return dziesietna;
}

// Testy
function test() {
  // Test konwersji dziesiętnej na binarną
  let dziesietna = 3;
  let oczekiwanaBinarna = "11";
  let binarna = dziesietnaNaBinarna(dziesietna);
  assert(binarna === oczekiwanaBinarna, "Błąd dla ${dziesietna}");

  // Test konwersji binarnej na dziesiętną
  let binarna2 = "101";
  let oczekiwanaDziesietna = 5;
  let dziesietna2 = binarnaNaDziesietna(binarna2);
  assert(dziesietna2 === oczekiwanaDziesietna, "Błąd dla ${binarna2}");
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
}

test();
