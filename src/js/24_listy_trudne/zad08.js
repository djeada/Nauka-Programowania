/*

Tytul: Sznurek.

Tresc: Masz do sprzedania sznurek o dlugosci n, a takze liste cen dla sznurkow o dlugosciach od 1 do n. Ceny moga byc rozne dla roznych dlugosci. Znajdz maksymalny zysk, ktory mozna osiagnac poprzez sprzedaz danego sznurka.

Dane wejsciowe: Lista n liczb calkowitych reprezentujacych ceny dla sznurkow o dlugosciach od 1 do n, oraz liczba naturalna n reprezentujaca dlugosc sznurka, ktory chcesz sprzedac.

Dane wyjsciowe: Najwieksza mozliwa wartosc, jaka mozna uzyskac ze sprzedazy danego sznurka.

Przyklad:

Dla listy cen: [1, 5, 8, 9, 10, 17, 17, 20] oraz dlugosci sznurka 4, powinna zostac zwrocona liczba 10.

*/

const sznurek = (lista, n) => {
  let max = 0;
  for (let i = 0; i < n; i++) {
    let suma = 0;
    for (let j = 0; j < n - i; j++) {
      suma += lista[j];
    }
    if (suma > max) {
      max = suma;
    }
  }
  return max;
};

// Testy
const lista1 = [1, 5, 8, 9, 10, 17, 17, 20];
const wynik1 = 10;
const lista2 = [3, 5, 8, 9, 10, 17, 17, 20];
const wynik2 = 22;

console.assert(sznurek(lista1, 4) === wynik1, "Test 1 nieudany");
console.assert(sznurek(lista2, 8) === wynik2, "Test 2 nieudany");

