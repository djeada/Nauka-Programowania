/*

Tytul: Sortowanie przez wybieranie.

Tresc: Napisz program sortujacy liste liczb calkowitych metoda sortowania przez wybieranie. Znajdz najwiekszy element w liscie i zapisz go do zmiennej. Nastepnie znajdz najmniejszy element w pozostalej czesci listy i zamien go z pierwszym elementem nieposortowanej czesci. Powtarzaj operacje, az lista bedzie posortowana.

Dane wejsciowe: Lista liczb calkowitych.

Dane wyjsciowe: Posortowana lista liczb calkowitych.

Przyklad:

Dla listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

*/

const sortowaniePrzezWybieranie = (lista) => {
  for (let i = 0; i < lista.length - 1; i++) {
    let indeksMin = i;
    for (let j = i + 1; j < lista.length; j++) {
      if (lista[j] < lista[indeksMin]) {
        indeksMin = j;
      }
    }
    if (indeksMin !== i) {
      [lista[i], lista[indeksMin]] = [lista[indeksMin], lista[i]];
    }
  }
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
  JSON.stringify(sortowaniePrzezWybieranie(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortowaniePrzezWybieranie(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
console.assert(
  JSON.stringify(sortowaniePrzezWybieranie(lista3)) === JSON.stringify(wynik3),
  "Test 3 nieudany"
);

