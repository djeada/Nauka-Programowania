/*

Tytul: Najdluzszy ciag jedynek.

Tresc: Otrzymujesz liste skladajaca sie wylacznie z zer i jedynek. Znajdz indeks zera, ktore po zamianie na jedynke daloby najdluzszy ciag jedynek. Jesli lista sklada sie wylacznie z zer lub wylacznie z jedynek, zwroc -1.

Dane wejsciowe: Lista liczb naturalnych.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanej listy: [0, 0, 1, 0, 1, 1, 1, 0, 1, 1], powinna zostac zwrocona liczba: 7.

*/

const najdluzszyCiagJedynek = (lista) => {
  let najdluzszyCiagJedynek = 0;
  let index = -1;
  let liczbaJedynek = 0;
  let indeks = 0;
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] === 1) {
      liczbaJedynek++;
    } else {
      indeks = i;
    }
    if (liczbaJedynek > najdluzszyCiagJedynek) {
      najdluzszyCiagJedynek = liczbaJedynek;
      index = indeks;
    }
  }
  return index;
};

// Testy
const lista1 = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1];
const wynik1 = 7;
const lista2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
const wynik2 = -1;

console.assert(najdluzszyCiagJedynek(lista1) === wynik1, "Test 1 nieudany");
console.assert(najdluzszyCiagJedynek(lista2) === wynik2, "Test 2 nieudany");

