/*
Tytul: Czy srednia elementow znajduje sie w liscie?

Tresc: Dla otrzymanej listy liczb calkowitych oraz liczby calkowitej jako klucza, usun pierwsze wystapienie klucza w liscie.

Dane wejsciowe: Lista liczb calkowitych i liczba calkowita jako klucz.

Dane wyjsciowe: Lista liczb calkowitych bez pierwszego wystapienia klucza.

Przyklad:

Dla otrzymanej listy [6, 2, 1, 4, 27] oraz 4 powinna zostac zwrocona lista [6, 2, 1, 27].
*/

function czySredniaWLiscie(lista) {
  let suma = 0;
  for (let i = 0; i < lista.length; i++) {
    suma += lista[i];
  }
  let srednia = suma / lista.length;
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] === srednia) {
      return true;
    }
  }
  return false;
}

// Testy

function testCzySredniaWLiscie_pozytywne() {
  console.assert(czySredniaWLiscie([6, 2, 1, 4, 27]) === true);
  console.assert(czySredniaWLiscie([2, 2, 2, 2, 2]) === true);
  console.assert(czySredniaWLiscie([1, 2, 3, 4, 5]) === true);
}

function testCzySredniaWLiscie_negatywne() {
  console.assert(czySredniaWLiscie([6, 2, 1, 27]) === false);
  console.assert(czySredniaWLiscie([2, 2, 2, 2]) === false);
  console.assert(czySredniaWLiscie([1, 2, 3, 4]) === false);
}

function main() {
  testCzySredniaWLiscie_pozytywne();
  testCzySredniaWLiscie_negatywne();
}

main();

