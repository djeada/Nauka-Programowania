/*

Tytul: Powtarzajace sie podnapisy.

Tresc: Dostajesz napis. Znajdz wszystkie powtarzajace sie podnapisy w tym napisie.

Dane wejsciowe: Napis.

Dane wyjsciowe: Lista napisow.

Przyklad:

Dla napisu "pythonpython" powinna zostac zwrocona lista zawierajaca napis "python".

*/

function powtarzajaceSiePodnapisy(napis) {
  const n = napis.length;
  const podnapisy = new Set();

  for (let len = Math.floor(n / 2); len >= 1; len--) {
    for (let i = 0; i <= n - len; i++) {
      const podnapis = napis.substring(i, i + len);
      const indexPowtorzenia = napis.indexOf(podnapis, i + 1);
      if (indexPowtorzenia !== -1) {
        podnapisy.add(podnapis);
      }
    }
  }
  return Array.from(podnapisy).sort();
}

function testPowtarzajaceSiePodnapisy() {
  const napis1 = "pythonpython";
  const wynik1 = [
    "h",
    "ho",
    "hon",
    "n",
    "o",
    "on",
    "p",
    "py",
    "pyt",
    "pyth",
    "pytho",
    "python",
    "t",
    "th",
    "tho",
    "thon",
    "y",
    "yt",
    "yth",
    "ytho",
    "ython",
  ];
  const napis2 = "abcabcabc";
  const wynik2 = [
    "a",
    "ab",
    "abc",
    "abca",
    "b",
    "bc",
    "bca",
    "bcab",
    "c",
    "ca",
    "cab",
    "cabc",
  ];

  console.assert(
    JSON.stringify(powtarzajaceSiePodnapisy(napis1)) === JSON.stringify(wynik1),
    "Test 1 nieudany"
  );
  console.assert(
    JSON.stringify(powtarzajaceSiePodnapisy(napis2)) === JSON.stringify(wynik2),
    "Test 2 nieudany"
  );
}

testPowtarzajaceSiePodnapisy();

