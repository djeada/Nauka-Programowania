/*

Tytul: Sortowanie slow w zdaniu.

Tresc: Masz dany napis reprezentujacy zdanie. Podziel to zdanie na slowa, posortuj je alfabetycznie i zapisz w liscie. Znaki interpunkcyjne nie sa liczone jako slowa.

Dane wejsciowe: Napis.

Dane wyjsciowe: Lista napisow.

Przyklad:

Dla napisu "Lemur wygina smialo cialo" powinno zostac zwrocone ["Lemur", "cialo", "smialo", "wygina"].

*/

const sortowanieSlow = (napis) => {
  return napis.split(" ").sort((a, b) => a.localeCompare(b));
};

// Testy
const napis1 = "Lemur wygina smialo cialo";
const wynik1 = ["Lemur", "cialo", "smialo", "wygina"];
const napis2 = "Ala ma kota a kot ma Ale";
const wynik2 = ["Ala", "Ale", "a", "kot", "kota", "ma", "ma"];

console.assert(
  JSON.stringify(sortowanieSlow(napis1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortowanieSlow(napis2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);

