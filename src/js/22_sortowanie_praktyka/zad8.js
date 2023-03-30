/*

Tytul: Wyszukiwanie indeksu klucza w cyklicznie posortowanej liscie.

Tresc: Otrzymujesz cyklicznie posortowana liste oraz klucz. Znajdz indeks pierwszego wystapienia klucza w liscie. Jesli klucz nie wystepuje w liscie, zwroc -1.

Dane wejsciowe: Cyklicznie posortowana lista, klucz.

Dane wyjsciowe: Indeks pierwszego wystapienia klucza lub -1.

Przyklad:

Dla cyklicznie posortowanej listy [3, 4, 5, 6, 1, 2] i klucza 4, powinno zostac zwrocone 2.

*/

const szukaj = (lista, klucz) => {
  let start = 0;
  let koniec = lista.length - 1;

  while (start <= koniec) {
    const srodek = Math.floor((start + koniec) / 2);

    if (lista[srodek] === klucz) {
      return srodek;
    }

    if (lista[start] <= lista[srodek]) {
      if (lista[start] <= klucz && klucz < lista[srodek]) {
        koniec = srodek - 1;
      } else {
        start = srodek + 1;
      }
    } else {
      if (lista[srodek] < klucz && klucz <= lista[koniec]) {
        start = srodek + 1;
      } else {
        koniec = srodek - 1;
      }
    }
  }

  return -1;
};

// Testy
const lista1 = [3, 4, 5, 6, 1, 2];
const klucz1 = 4;
const wynik1 = 1;

const lista2 = [4, 5, 6, 7, 8, 9, 1, 2, 3];
const klucz2 = 6;
const wynik2 = 2;

console.assert(szukaj(lista1, klucz1) === wynik1, "Test 1 nieudany");
console.assert(szukaj(lista2, klucz2) === wynik2, "Test 2 nieudany");

