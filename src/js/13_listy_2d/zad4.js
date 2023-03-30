/*
Tytuł: Dodawanie i odejmowanie macierzy.

Treść: Otrzymujesz dwie macierze o tych samych wymiarach. Zwróć dwie macierze będące:

a) wynikiem dodawania otrzymanych macierzy

b) wynikiem odejmowania drugiej macierzy od pierwszej.

Dane wejściowe: Dwie listy list liczb naturalnych.

Dane wyjściowe: Dwie listy list liczb naturalnych.

Przykład:

Dla otrzymanych dwóch macierzy: [[1, 2], [-2, 0]] oraz [[5, -3], [1, 7]], powinny zostać zwrócone następujące macierze:

a) [[6, -1], [-1, 7]] - wynik dodawania

b) [[-4, 5], [-3, -7]] - wynik odejmowania drugiej macierzy od pierwszej.
*/
function dodajMacierze(macierzA, macierzB) {
  const wynik = [];
  for (let i = 0; i < macierzA.length; i++) {
    const wiersz = [];
    for (let j = 0; j < macierzA[i].length; j++) {
      wiersz.push(macierzA[i][j] + macierzB[i][j]);
    }
    wynik.push(wiersz);
  }
  return wynik;
}

function odejmijMacierze(macierzA, macierzB) {
  const wynik = [];
  for (let i = 0; i < macierzA.length; i++) {
    const wiersz = [];
    for (let j = 0; j < macierzA[i].length; j++) {
      wiersz.push(macierzA[i][j] - macierzB[i][j]);
    }
    wynik.push(wiersz);
  }
  return wynik;
}

// test
function testDodajMacierze() {
  const macierzA = [
    [1, 2],
    [-2, 0],
  ];
  const macierzB = [
    [5, -3],
    [1, 7],
  ];
  const wynikDodawania = [
    [6, -1],
    [-1, 7],
  ];
  const dodawanie = dodajMacierze(macierzA, macierzB);
  for (let i = 0; i < dodawanie.length; i++) {
    for (let j = 0; j < dodawanie[i].length; j++) {
      console.assert(
        dodawanie[i][j] === wynikDodawania[i][j],
        `Element macierzy o indeksie (${i}, ${j}) nie jest taki sam jak w oczekiwanej macierzy. Oczekiwano: ${wynikDodawania[i][j]}, otrzymano: ${dodawanie[i][j]}.`
      );
    }
  }
}

function testOdejmijMacierze() {
  const macierzA = [
    [1, 2],
    [-2, 0],
  ];
  const macierzB = [
    [5, -3],
    [1, 7],
  ];
  const wynikOdejmowania = [
    [-4, 5],
    [-3, -7],
  ];
  const odejmowanie = odejmijMacierze(macierzA, macierzB);
  for (let i = 0; i < odejmowanie.length; i++) {
    for (let j = 0; j < odejmowanie[i].length; j++) {
      console.assert(
        odejmowanie[i][j] === wynikOdejmowania[i][j],
        "Element macierzy o indeksie (${i}, ${j}) nie jest taki sam jak w oczekiwanej macierzy. Oczekiwano: ${wynikOdejmowania[i][j]}, otrzymano: ${odejmowanie[i][j]}."
      );
    }
  }
}

testDodajMacierze();
testOdejmijMacierze();
