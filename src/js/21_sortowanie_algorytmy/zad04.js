/*

Tytul: Sortowanie przez scalanie.

Tresc: Dla danej listy liczb calkowitych zaimplementuj algorytm sortowania przez scalanie.

1. Jesli dlugosc listy jest mniejsza niz 2, zwroc liste.
2. Podziel liste na dwie rowne (lub prawie rowne) czesci.
3. Wywolaj rekurencyjnie sortowanie przez scalanie dla obu czesci listy.
4. Scal obie posortowane czesci listy w jedna posortowana liste.

Dane wejsciowe: Lista liczb calkowitych.

Dane wyjsciowe: Posortowana lista liczb calkowitych.

Przyklad:

Dla danej listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

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

// Testy
const lista1 = [6, 2, 1, 4, 27];
const wynik1 = [1, 2, 4, 6, 27];
const lista2 = [5, 4, 3, 2, 1];
const wynik2 = [1, 2, 3, 4, 5];
const lista3 = [-3, 0, 15, -7, 23];
const wynik3 = [-7, -3, 0, 15, 23];

console.assert(
  JSON.stringify(sortowaniePrzezScalanie(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortowaniePrzezScalanie(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
console.assert(
  JSON.stringify(sortowaniePrzezScalanie(lista3)) === JSON.stringify(wynik3),
  "Test 3 nieudany"
);

