/*

Tytuł: Anagramy w tekście

Otrzymujesz tekst w postaci napisu. Twoim zadaniem jest znalezienie wszystkich słów, w których te same znaki występują tę samą liczbę razy. Innymi słowy, szukasz anagramów w tekście. Należy zignorować różnice między małymi i wielkimi literami. Pamiętaj, że słowa składają się wyłącznie z liter.

Dane wejściowe: Napis.

Dane wyjściowe: Lista list napisów.

Przykład:

Dla otrzymanego napisu:

"To absurd, że tyran Brudas, ten straszliwy bandzior sprawuje rządy w tym kraju. Burza nad galerią i alergia na narty to żadna zbrodnia jak bandzior i jego arbuz.",

powinna zostać zwrócona lista:

[["absurd", "brudas"], ["tyran", "narty"], ["bandzior", "zbrodnia"], ["burza", "arbuz"], ["galeria", "alergia"]].
*/

function anagramyWTekscie(tekst) {
  const slowa = tekst.match(/[a-z]+/gi);
  const anagramy = {};
  for (const slowo of slowa) {
    const klucz = slowo.toLowerCase().split("").sort().join("");
    if (!anagramy[klucz]) {
      anagramy[klucz] = [slowo];
    } else {
      anagramy[klucz].push(slowo);
    }
  }
  const wynik = Object.values(anagramy);
  return wynik.filter((anagram) => anagram.length > 1);
}

function testAnagramyWTekscie() {
  const tekst =
    "To absurd, że tyran Brudas, ten straszliwy bandzior sprawuje rządy w tym kraju. Burza nad galerią i alergia na narty to żadna zbrodnia jak bandzior i jego arbuz.";
  const wynik = anagramyWTekscie(tekst);
  const poprawnyWynik = [
    ["absurd", "brudas"],
    ["tyran", "narty"],
    ["bandzior", "zbrodnia"],
    ["burza", "arbuz"],
    ["galeria", "alergia"],
  ];
  console.assert(wynik.length === poprawnyWynik.length, "Test nie powiódł się");
  for (const anagram of wynik) {
    const poprawnyAnagram = poprawnyWynik.find(
      (pa) => pa.length === anagram.length && pa.includes(anagram[0])
    );
    console.assert(poprawnyAnagram, "Test nie powiódł się");
  }
}

testAnagramyWTekscie();
