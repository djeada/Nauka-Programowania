/*

Tytuł: Wspólny podciąg o największej sumie.

Treść: Otrzymujesz dwie listy binarne, A oraz B. Znajdź największą długość takich dwóch podciągów, które dla obu list zaczynają się i kończą na tej samej pozycji i których suma elementów jest jednakowa.

Dane wejściowe: Dwie listy binarne.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanych list: [0, 0, 1, 1, 1, 1] i [0, 1, 1, 0, 1, 0], powinna zostać zwrócona liczba: 5.

Wyjaśnienia: Suma elementów obu list na pozycjach od 0 do 4 jest równa 3.


*/

const wspolnyPodciagONajwiekszejSumie = (lista1, lista2) => {
  let max = 0;
  for (let i = 0; i < lista1.length; i++) {
    for (let j = i; j < lista1.length; j++) {
      let suma1 = 0;
      let suma2 = 0;
      for (let k = i; k <= j; k++) {
        suma1 += lista1[k];
        suma2 += lista2[k];
      }
      if (suma1 === suma2 && j - i + 1 > max) {
        max = j - i + 1;
      }
    }
  }
  return max;
};

const assert = (condition, message) => {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
};

// Testy
const lista1 = [0, 0, 1, 1, 1, 1];
const lista2 = [0, 1, 1, 0, 1, 0];
const wynik = 5;

assert(
  wspolnyPodciagONajwiekszejSumie(lista1, lista2) === wynik,
  "Test 1 nieudany"
);
