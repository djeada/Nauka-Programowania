/*


Tytul: Powtarzajace sie znaki

Otrzymujesz napis. Twoim zadaniem jest znalezienie i zwrocenie wszystkich znakow, ktore wystepuja co najmniej 2 razy w ciagu.

Dane wejsciowe: Napis.

Dane wyjsciowe: Napis.

Przyklad:

Dla otrzymanego napisu: "aaabbbccc"

Powinien zostac zwrocony napis: "abc"
*/

function powtarzajaceSieZnaki(napis) {
  const znaki = {};
  let powtarzajaceSie = "";
  for (let i = 0; i < napis.length; i++) {
    const znak = napis[i];
    if (!znaki[znak]) {
      znaki[znak] = 1;
    } else {
      znaki[znak]++;
    }
  }
  for (const znak in znaki) {
    if (znaki[znak] >= 2) {
      powtarzajaceSie += znak;
    }
  }
  return powtarzajaceSie;
}

function testPowtarzajaceSieZnaki() {
  const napis1 = "aaabbbccc";
  const wynik1 = powtarzajaceSieZnaki(napis1);
  console.assert(wynik1 === "abc", "Test 1 nie powiodl sie");

  const napis2 = "abcd";
  const wynik2 = powtarzajaceSieZnaki(napis2);
  console.assert(wynik2 === "", "Test 2 nie powiodl sie");

  const napis3 = "Ala ma kota, a kot ma Ale.";
  const wynik3 = powtarzajaceSieZnaki(napis3);
  console.assert(wynik3 === "aekmt", "Test 3 nie powiodl sie");
}

testPowtarzajaceSieZnaki();

