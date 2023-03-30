/*

Tytul: Najdluzszy naprzemienny podciag.

Tresc: Masz dana liste liczb. Znajdz najdluzszy podciag naprzemienny w tej liscie. Ciag jest naprzemienny, jesli liczby w nim rosna i maleja na zmiane. Na przyklad [1, 3, 2, 4, 3, 5] jest naprzemienny.

Dane wejsciowe: Lista n liczb calkowitych.

Dane wyjsciowe: Lista liczb calkowitych reprezentujaca najdluzszy podciag naprzemienny w tej liscie.

Przyklad:

Dla listy liczb: [1, -2, 6, 4, -3, 2, -4, -3], powinna zostac zwrocona lista [1, -2, 6, -3, 2, -4].


*/

const najdluzszyNaprzemiennyPodciag = (lista) => {
  let result = [];
  let temp = [];
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] > lista[i + 1]) {
      temp.push(lista[i]);
      if (temp.length > result.length) {
        result = temp;
      }
    } else {
      temp = [];
    }
  }
  return result;
};

// Testy
const lista1 = [1, -2, 6, 4, -3, 2, -4, -3];
const wynik1 = [1, -2, 6, -3, 2, -4];
const lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const wynik2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];

console.assert(
  JSON.stringify(najdluzszyNaprzemiennyPodciag(lista1)) ===
    JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(najdluzszyNaprzemiennyPodciag(lista2)) ===
    JSON.stringify(wynik2),
  "Test 2 nieudany"
);

