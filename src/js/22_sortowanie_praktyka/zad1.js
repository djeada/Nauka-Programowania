/*

Tytul: Sortowanie znakow w napisie.

Tresc: Otrzymujesz napis. Posortuj alfabetycznie jego znaki.

Dane wejsciowe: Napis.

Dane wyjsciowe: Napis.

Przyklad:

Dla napisu "Ala ma kota" powinno zostac zwrocone " Aaaaklmot".

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
const napis3 = "zazolc";
const wynik3 = "azlozz";

console.assert(sortowanieZnakow(napis1) === wynik1, "Test 1 nieudany");
console.assert(sortowanieZnakow(napis2) === wynik2, "Test 2 nieudany");
console.assert(sortowanieZnakow(napis3) === wynik3, "Test 3 nieudany");

