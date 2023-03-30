/*

Tytul: Anagramy w tekscie

Otrzymujesz tekst w postaci napisu. Twoim zadaniem jest znalezienie wszystkich slow, w ktorych te same znaki wystepuja te sama liczbe razy. Innymi slowy, szukasz anagramow w tekscie. Nalezy zignorowac roznice miedzy malymi i wielkimi literami. Pamietaj, ze slowa skladaja sie wylacznie z liter.

Dane wejsciowe: Napis.

Dane wyjsciowe: Lista list napisow.

Przyklad:

Dla otrzymanego napisu:

"To absurd, ze tyran Brudas, ten straszliwy bandzior sprawuje rzady w tym kraju. Burza nad galeria i alergia na narty to zadna zbrodnia jak bandzior i jego arbuz.",

powinna zostac zwrocona lista:

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
    "To absurd, ze tyran Brudas, ten straszliwy bandzior sprawuje rzady w tym kraju. Burza nad galeria i alergia na narty to zadna zbrodnia jak bandzior i jego arbuz.";
  const wynik = anagramyWTekscie(tekst);
  const poprawnyWynik = [
    ["absurd", "brudas"],
    ["tyran", "narty"],
    ["bandzior", "zbrodnia"],
    ["burza", "arbuz"],
    ["galeria", "alergia"],
  ];
  console.assert(wynik.length === poprawnyWynik.length, "Test nie powiodl sie");
  for (const anagram of wynik) {
    const poprawnyAnagram = poprawnyWynik.find(
      (pa) => pa.length === anagram.length && pa.includes(anagram[0])
    );
    console.assert(poprawnyAnagram, "Test nie powiodl sie");
  }
}

testAnagramyWTekscie();

