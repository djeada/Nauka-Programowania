/*

Tytul: Sortowanie babelkowe.

Tresc: Napisz program sortujacy liste liczb calkowitych metoda sortowania babelkowego. Porownaj sasiednie liczby z listy i zamien je miejscami, jesli pierwsza jest wieksza od drugiej. Powtarzaj operacje, az przejdziesz przez cala liste bez dokonywania zmian.

Dane wejsciowe: Lista liczb calkowitych.

Dane wyjsciowe: Posortowana lista liczb calkowitych.

Przyklad:

Dla listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

*/

const sortowanieBabelkowe = (lista) => {
  let zamiana;
  do {
    zamiana = false;
    for (let i = 0; i < lista.length - 1; i++) {
      if (lista[i] > lista[i + 1]) {
        [lista[i], lista[i + 1]] = [lista[i + 1], lista[i]];
        zamiana = true;
      }
    }
  } while (zamiana);
  return lista;
};

// Testy
const lista1 = [6, 2, 1, 4, 27];
const wynik1 = [1, 2, 4, 6, 27];
const lista2 = [5, 4, 3, 2, 1];
const wynik2 = [1, 2, 3, 4, 5];
const lista3 = [-3, 0, 15, -7, 23];
const wynik3 = [-7, -3, 0, 15, 23];

console.assert(
  JSON.stringify(sortowanieBabelkowe(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortowanieBabelkowe(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
console.assert(
  JSON.stringify(sortowanieBabelkowe(lista3)) === JSON.stringify(wynik3),
  "Test 3 nieudany"
);

