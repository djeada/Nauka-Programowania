/*
Tytul: Pierwsze wystapienie klucza.

Tresc: Otrzymujesz liste liczb naturalnych oraz liczbe naturalna jako klucz. Znajdz indeks odpowiadajacy pierwszemu wystapieniu klucza w liscie. Jesli klucz nie wystepuje w liscie, zwroc -1.

Dane wejsciowe: Lista liczb naturalnych oraz liczba naturalna jako klucz.

Dane wyjsciowe: Liczba calkowita oznaczajaca indeks pierwszego wystapienia klucza w liscie.

Przyklad:

Dla otrzymanej listy [2, 9, -1, 3, 8] oraz klucza -1 powinno zostac zwrocone 2.
*/

function pierwszeWystapienieKlucza(lista, klucz) {
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] === klucz) {
      return i;
    }
  }
  return -1;
}

// Testy

function testPierwszeWystapienieKlucza_pozytywne() {
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], -1) === 2);
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], 9) === 1);
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], 2) === 0);
}

function testPierwszeWystapienieKlucza_negatywne() {
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], 0) === -1);
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], 10) === -1);
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], 100) === -1);
}

function main() {
  testPierwszeWystapienieKlucza_pozytywne();
  testPierwszeWystapienieKlucza_negatywne();
}

main();

