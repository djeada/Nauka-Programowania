/*
Tytul: Konwersja pomiedzy systemami binarnym i dziesietnym.

Tresc:

a) Otrzymujesz reprezentacje dziesietna liczby naturalnej, zwroc jej reprezentacje binarna.

b) Otrzymujesz reprezentacje binarna liczby naturalnej, zwroc jej reprezentacje dziesietna.

Dane wejsciowe: Liczba naturalna w obu podpunktach.

Dane wyjsciowe: Liczba naturalna w obu podpunktach.

Przyklad:

a) Dla otrzymanej liczby: 3, powinna zostac zwrocona liczba: 11.

b) Dla otrzymanej liczby: 101, powinna zostac zwrocona liczba: 5.
*/

// a) Konwersja liczby dziesietnej na binarna
function dziesietnaNaBinarna(dziesietna) {
  let binarna = "";
  while (dziesietna > 0) {
    binarna = (dziesietna % 2) + binarna;
    dziesietna = Math.floor(dziesietna / 2);
  }
  return binarna === "" ? "0" : binarna;
}

// b) Konwersja liczby binarnej na dziesietna
function binarnaNaDziesietna(binarna) {
  let dziesietna = 0;
  for (let i = 0; i < binarna.length; i++) {
    dziesietna += parseInt(binarna[i]) * Math.pow(2, binarna.length - i - 1);
  }
  return dziesietna;
}

// Testy
function test() {
  // Test konwersji dziesietnej na binarna
  let dziesietna = 3;
  let oczekiwanaBinarna = "11";
  let binarna = dziesietnaNaBinarna(dziesietna);
  console.assert(binarna === oczekiwanaBinarna, "Blad dla ${dziesietna}");

  // Test konwersji binarnej na dziesietna
  let binarna2 = "101";
  let oczekiwanaDziesietna = 5;
  let dziesietna2 = binarnaNaDziesietna(binarna2);
  console.assert(dziesietna2 === oczekiwanaDziesietna, "Blad dla ${binarna2}");
}

test();

