/*


Tytuł: Powtarzające się znaki

Otrzymujesz napis. Twoim zadaniem jest znalezienie i zwrócenie wszystkich znaków, które występują co najmniej 2 razy w ciągu.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanego napisu: "aaabbbccc"

Powinien zostać zwrócony napis: "abc"
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
  assert(wynik1 === "abc", "Test 1 nie powiódł się");

  const napis2 = "abcd";
  const wynik2 = powtarzajaceSieZnaki(napis2);
  assert(wynik2 === "", "Test 2 nie powiódł się");

  const napis3 = "Ala ma kota, a kot ma Ale.";
  const wynik3 = powtarzajaceSieZnaki(napis3);
  assert(wynik3 === "aekmt", "Test 3 nie powiódł się");
}

// test
function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Asercja nie powiodła się");
  }
}

testPowtarzajaceSieZnaki();
