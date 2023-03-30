/*

Tytul: Wspolny podciag o najwiekszej sumie.

Tresc: Otrzymujesz dwie listy binarne, A oraz B. Znajdz najwieksza dlugosc takich dwoch podciagow, ktore dla obu list zaczynaja sie i koncza na tej samej pozycji i ktorych suma elementow jest jednakowa.

Dane wejsciowe: Dwie listy binarne.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanych list: [0, 0, 1, 1, 1, 1] i [0, 1, 1, 0, 1, 0], powinna zostac zwrocona liczba: 5.

Wyjasnienia: Suma elementow obu list na pozycjach od 0 do 4 jest rowna 3.


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

// Testy
const lista1 = [0, 0, 1, 1, 1, 1];
const lista2 = [0, 1, 1, 0, 1, 0];
const wynik = 5;

console.assert(
  wspolnyPodciagONajwiekszejSumie(lista1, lista2) === wynik,
  "Test 1 nieudany"
);

