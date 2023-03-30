/*
Tytul: Usun duplikaty.

Tresc: Otrzymujesz liste liczb naturalnych. Usun z niej wszystkie duplikaty, tak aby kazda liczba pozostala tylko raz.

Dane wejsciowe: Lista liczb naturalnych.

Dane wyjsciowe: Lista liczb naturalnych.

Przyklad:

Dla otrzymanej listy: [3, 2, 1, 3, 2, 2], powinna zostac zwrocona lista: [3, 2, 1].

*/

function usunDuplikaty(lista) {
  var wynik = [];

  for (var i = 0; i < lista.length; i++) {
    if (wynik.indexOf(lista[i]) === -1) {
      wynik.push(lista[i]);
    }
  }

  return wynik;
}

// Testy

function testUsunDuplikaty() {
  console.assert(
    usunDuplikaty([3, 2, 1, 3, 2, 2]).toString() === [3, 2, 1].toString()
  );
  console.assert(
    usunDuplikaty([1, 2, 3, 4, 5, 6]).toString() ===
      [1, 2, 3, 4, 5, 6].toString()
  );
  console.assert(
    usunDuplikaty([6, 5, 4, 3, 2, 1]).toString() ===
      [6, 5, 4, 3, 2, 1].toString()
  );
}

function main() {
  testUsunDuplikaty();
}

main();

