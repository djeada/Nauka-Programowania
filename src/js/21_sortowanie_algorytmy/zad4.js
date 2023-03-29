/*

Tytuł: Sortowanie przez scalanie.

Treść: Dla danej listy liczb całkowitych zaimplementuj algorytm sortowania przez scalanie.

1. Jeśli długość listy jest mniejsza niż 2, zwróć listę.
2. Podziel listę na dwie równe (lub prawie równe) części.
3. Wywołaj rekurencyjnie sortowanie przez scalanie dla obu części listy.
4. Scal obie posortowane części listy w jedną posortowaną listę.

Dane wejściowe: Lista liczb całkowitych.

Dane wyjściowe: Posortowana lista liczb całkowitych.

Przykład:

Dla danej listy: [6, 2, 1, 4, 27], powinna zostać zwrócona lista: [1, 2, 4, 6, 27].

*/

const scalanie = (lewa, prawa) => {
  let scalonaLista = [];
  let lewyIndeks = 0;
  let prawyIndeks = 0;

  while (lewyIndeks < lewa.length && prawyIndeks < prawa.length) {
    if (lewa[lewyIndeks] < prawa[prawyIndeks]) {
      scalonaLista.push(lewa[lewyIndeks]);
      lewyIndeks++;
    } else {
      scalonaLista.push(prawa[prawyIndeks]);
      prawyIndeks++;
    }
  }

  return scalonaLista
    .concat(lewa.slice(lewyIndeks))
    .concat(prawa.slice(prawyIndeks));
};

const sortowaniePrzezScalanie = (lista) => {
  if (lista.length < 2) {
    return lista;
  }

  const srodek = Math.floor(lista.length / 2);
  const lewa = lista.slice(0, srodek);
  const prawa = lista.slice(srodek);

  return scalanie(
    sortowaniePrzezScalanie(lewa),
    sortowaniePrzezScalanie(prawa)
  );
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
  JSON.stringify(sortowaniePrzezScalanie(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
assert(
  JSON.stringify(sortowaniePrzezScalanie(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
assert(
  JSON.stringify(sortowaniePrzezScalanie(lista3)) === JSON.stringify(wynik3),
  "Test 3 nieudany"
);
