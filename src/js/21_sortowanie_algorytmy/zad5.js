/*

Tytul: Sortowanie szybkie.

Tresc: Dla danej listy liczb calkowitych zaimplementuj algorytm sortowania szybkiego.

1. Jesli dlugosc listy jest mniejsza niz 2, zwroc liste.
2. Wybierz element rozdzielajacy, nazywany pivotem.
3. Podziel liste na trzy czesci: elementy mniejsze od pivota, pivot oraz elementy wieksze od pivota.
4. Wywolaj rekurencyjnie sortowanie szybkie dla czesci z elementami mniejszymi od pivota i wiekszymi od pivota.
5. Scal posortowane czesci listy w jedna posortowana liste.

Dane wejsciowe: Lista liczb calkowitych.

Dane wyjsciowe: Posortowana lista liczb calkowitych.

Przyklad:

Dla danej listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

*/

const sortowanieSzybkie = (lista) => {
  if (lista.length < 2) {
    return lista;
  }

  const pivotIndeks = Math.floor(Math.random() * lista.length);
  const pivot = lista[pivotIndeks];

  const mniejsze = [];
  const wieksze = [];
  const pivots = [];

  for (const element of lista) {
    if (element < pivot) {
      mniejsze.push(element);
    } else if (element > pivot) {
      wieksze.push(element);
    } else {
      pivots.push(element);
    }
  }

  return sortowanieSzybkie(mniejsze)
    .concat(pivots)
    .concat(sortowanieSzybkie(wieksze));
};

// Testy
const lista1 = [6, 2, 1, 4, 27];
const wynik1 = [1, 2, 4, 6, 27];
const lista2 = [5, 4, 3, 2, 1];
const wynik2 = [1, 2, 3, 4, 5];
const lista3 = [-3, 0, 15, -7, 23];
const wynik3 = [-7, -3, 0, 15, 23];

console.assert(
  JSON.stringify(sortowanieSzybkie(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortowanieSzybkie(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
console.assert(
  JSON.stringify(sortowanieSzybkie(lista3)) === JSON.stringify(wynik3),
  "Test 3 nieudany"
);

