/*

Tytuł: Sortowanie słów w zdaniu.

Treść: Masz dany napis reprezentujący zdanie. Podziel to zdanie na słowa, posortuj je alfabetycznie i zapisz w liście. Znaki interpunkcyjne nie są liczone jako słowa.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla napisu "Lemur wygina śmiało ciało" powinno zostać zwrócone ["Lemur", "ciało", "śmiało", "wygina"].

*/

const sortowanieSlow = (napis) => {
  return napis.split(" ").sort((a, b) => a.localeCompare(b));
};

const assert = (condition, message) => {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
};

// Testy
const napis1 = "Lemur wygina śmiało ciało";
const wynik1 = ["Lemur", "ciało", "śmiało", "wygina"];
const napis2 = "Ala ma kota a kot ma Alę";
const wynik2 = ["Ala", "Alę", "a", "kot", "kota", "ma", "ma"];

assert(
  JSON.stringify(sortowanieSlow(napis1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
assert(
  JSON.stringify(sortowanieSlow(napis2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
