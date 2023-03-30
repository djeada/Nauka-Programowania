/*
Tytul: Usun klucz.

Tresc: Dla otrzymanej listy: liczb calkowitych oraz klucza, usun pierwsze wystapienie klucza w liscie.

Dane wejsciowe: Lista liczb calkowitych i liczba calkowita.

Dane wyjsciowe: Lista liczb calkowitych.

Przyklad:

Dla otrzymanej listy: [6, 2, 1, 4, 27] oraz 4, powinna zostac zwrocona lista: [6, 2, 1, 27].

*/

function usunKlucz(lista, klucz) {
  let wynik = [];
  let czyZnaleziono = false;
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] === klucz && !czyZnaleziono) {
      czyZnaleziono = true;
    } else {
      wynik.push(lista[i]);
    }
  }
  return wynik;
}

// Testy

function testUsunKlucz() {
  console.assert(
    usunKlucz([6, 2, 1, 4, 27], 4).toString() === [6, 2, 1, 27].toString()
  );
  console.assert(
    usunKlucz([6, 2, 1, 4, 27], 6).toString() === [2, 1, 4, 27].toString()
  );
  console.assert(
    usunKlucz([6, 2, 1, 4, 27], 27).toString() === [6, 2, 1, 4].toString()
  );
}

function main() {
  testUsunKlucz();
}

main();

