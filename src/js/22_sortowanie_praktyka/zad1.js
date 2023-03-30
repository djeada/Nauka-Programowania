/*

Tytuł: Sortowanie znaków w napisie.

Treść: Otrzymujesz napis. Posortuj alfabetycznie jego znaki.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla napisu "Ala ma kota" powinno zostać zwrócone " Aaaaklmot".

*/

const sortowanieZnakow = (napis) => {
  return napis
    .split("")
    .sort((a, b) => a.localeCompare(b))
    .join("");
};

// Testy
const napis1 = "Ala ma kota";
const wynik1 = " Aaaaklmot";
const napis2 = "Javascript";
const wynik2 = "Jaaaciprstv";
const napis3 = "zażółć";
const wynik3 = "ażłózż";

console.assert(sortowanieZnakow(napis1) === wynik1, "Test 1 nieudany");
console.assert(sortowanieZnakow(napis2) === wynik2, "Test 2 nieudany");
console.assert(sortowanieZnakow(napis3) === wynik3, "Test 3 nieudany");
