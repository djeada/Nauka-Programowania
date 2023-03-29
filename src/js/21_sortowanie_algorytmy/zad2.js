/*

Tytuł: Sortowanie przez wybieranie.

Treść: Napisz program sortujący listę liczb całkowitych metodą sortowania przez wybieranie. Znajdź największy element w liście i zapisz go do zmiennej. Następnie znajdź najmniejszy element w pozostałej części listy i zamień go z pierwszym elementem nieposortowanej części. Powtarzaj operację, aż lista będzie posortowana.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Posortowana lista liczb całkowitych.

Przykład:

Dla listy: [6, 2, 1, 4, 27], powinna zostać zwrócona lista: [1, 2, 4, 6, 27].

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

const assert = (condition, message) => {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
};

// Testy
const lista1 = [6, 2, 1, 4, 27];
const wynik1 = [1, 2, 4, 6, 27];
const lista2 = [5, 4, 3, 2, 1];
const wynik2 = [1, 2, 3, 4, 5];
const lista3 = [-3, 0, 15, -7, 23];
const wynik3 = [-7, -3, 0, 15, 23];

assert(
  JSON.stringify(sortowaniePrzezWybieranie(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
assert(
  JSON.stringify(sortowaniePrzezWybieranie(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
assert(
  JSON.stringify(sortowaniePrzezWybieranie(lista3)) === JSON.stringify(wynik3),
  "Test 3 nieudany"
);
