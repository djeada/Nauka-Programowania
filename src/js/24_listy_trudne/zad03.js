/*

Tytul: Minimalny iloczyn.

Tresc: Otrzymujesz liste liczb calkowitych. Znajdz najmniejszy iloczyn dla trzech liczb wybranych z listy. Jesli lista sklada sie z mniej niz trzech liczb, zwroc iloczyn wszystkich elementow listy.

Dane wejsciowe: Lista liczb calkowitych.

Dane wyjsciowe: Liczba calkowita.

Przyklad:

Dla otrzymanej listy: [3, -1, -3, 2, 9, 4], powinna zostac zwrocona liczba: -108.

*/

const minimalnyIloczyn = (lista) => {
  let min = lista[0] * lista[1] * lista[2];
  for (let i = 0; i < lista.length; i++) {
    for (let j = i + 1; j < lista.length; j++) {
      for (let k = j + 1; k < lista.length; k++) {
        if (lista[i] * lista[j] * lista[k] < min) {
          min = lista[i] * lista[j] * lista[k];
        }
      }
    }
  }
  return min;
};

// Testy
const lista1 = [3, -1, -3, 2, 9, 4];
const wynik1 = -108;
const lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const wynik2 = 6;

console.assert(minimalnyIloczyn(lista1) === wynik1, "Test 1 nieudany");
console.assert(minimalnyIloczyn(lista2) === wynik2, "Test 2 nieudany");

