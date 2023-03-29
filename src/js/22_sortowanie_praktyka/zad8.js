/*

Tytuł: Wyszukiwanie indeksu klucza w cyklicznie posortowanej liście.

Treść: Otrzymujesz cyklicznie posortowaną listę oraz klucz. Znajdź indeks pierwszego wystąpienia klucza w liście. Jeśli klucz nie występuje w liście, zwróć -1.

Dane wejściowe: Cyklicznie posortowana lista, klucz.

Dane wyjściowe: Indeks pierwszego wystąpienia klucza lub -1.

Przykład:

Dla cyklicznie posortowanej listy [3, 4, 5, 6, 1, 2] i klucza 4, powinno zostać zwrócone 2.

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

const assert = (condition, message) => {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
};

// Testy
const lista1 = [3, 4, 5, 6, 1, 2];
const klucz1 = 4;
const wynik1 = 1;

const lista2 = [4, 5, 6, 7, 8, 9, 1, 2, 3];
const klucz2 = 6;
const wynik2 = 2;

assert(szukaj(lista1, klucz1) === wynik1, "Test 1 nieudany");
assert(szukaj(lista2, klucz2) === wynik2, "Test 2 nieudany");
