/*

Tytul: Sortowanie przez wstawianie.

Tresc: Napisz program sortujacy liste liczb calkowitych metoda sortowania przez wstawianie. Stworz nowa, pusta liste i dodaj do niej pierwszy element listy wejsciowej. Dla kazdego kolejnego elementu znajdz odpowiednie miejsce w posortowanej juz czesci listy i wstaw go tam.

Dane wejsciowe: Lista liczb calkowitych.

Dane wyjsciowe: Posortowana lista liczb calkowitych.

Przyklad:

Dla listy: [6, 2, 1, 4, 27], powinna zostac zwrocona lista: [1, 2, 4, 6, 27].

*/

const sortowaniePrzezWstawianie = (lista) => {
  const posortowanaLista = [lista[0]];

  for (let i = 1; i < lista.length; i++) {
    let elementDoWstawienia = lista[i];
    let j;
    for (
      j = posortowanaLista.length - 1;
      j >= 0 && posortowanaLista[j] > elementDoWstawienia;
      j--
    ) {
      posortowanaLista[j + 1] = posortowanaLista[j];
    }
    posortowanaLista[j + 1] = elementDoWstawienia;
  }

  return posortowanaLista;
};

// Testy
const lista1 = [6, 2, 1, 4, 27];
const wynik1 = [1, 2, 4, 6, 27];
const lista2 = [5, 4, 3, 2, 1];
const wynik2 = [1, 2, 3, 4, 5];
const lista3 = [-3, 0, 15, -7, 23];
const wynik3 = [-7, -3, 0, 15, 23];

console.assert(
  JSON.stringify(sortowaniePrzezWstawianie(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortowaniePrzezWstawianie(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
console.assert(
  JSON.stringify(sortowaniePrzezWstawianie(lista3)) === JSON.stringify(wynik3),
  "Test 3 nieudany"
);

