/*

Tytuł: Zmiana wielkości liter.

Treść: Otrzymujesz napis. Zaimplementuj następujące operacje przy użyciu operatorów bitowych:

a) Zamień wielkie litery na małe litery.

b) Zamień małe litery na wielkie litery.

c) Zamień małe litery na wielkie litery i wielkie litery na małe litery.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

a) Dla otrzymanego napisu: "Test", powinien zostać zwrócony napis: "test".

b) Dla otrzymanego napisu: "Test", powinien zostać zwrócony napis: "TEST".

c) Dla otrzymanego napisu: "Test", powinien zostać zwrócony napis: "tEST".
*/

function zamienNaMaleLitery(napis) {
  let wynik = "";
  for (let i = 0; i < napis.length; i++) {
    const kod = napis.charCodeAt(i);
    if (kod >= 65 && kod <= 90) {
      wynik += String.fromCharCode(kod + 32);
    } else {
      wynik += napis[i];
    }
  }
  return wynik;
}

function zamienNaWielkieLitery(napis) {
  let wynik = "";
  for (let i = 0; i < napis.length; i++) {
    const kod = napis.charCodeAt(i);
    if (kod >= 97 && kod <= 122) {
      wynik += String.fromCharCode(kod - 32);
    } else {
      wynik += napis[i];
    }
  }
  return wynik;
}

function zamienLitery(napis) {
  let wynik = "";
  for (let i = 0; i < napis.length; i++) {
    const kod = napis.charCodeAt(i);
    if (kod >= 65 && kod <= 90) {
      wynik += String.fromCharCode(kod + 32);
    } else if (kod >= 97 && kod <= 122) {
      wynik += String.fromCharCode(kod - 32);
    } else {
      wynik += napis[i];
    }
  }
  return wynik;
}

// Testy

function testZamienNaMaleLitery() {
  const input = "TeST nAPIsu";
  const expectedOutput = "test napisu";
  const output = zamienNaMaleLitery(input);

  console.assert(
    output === expectedOutput,
    `Test nie powiódł się dla ${input}`
  );
  console.log("Test przeszedł pomyślnie");
}

function testZamienNaWielkieLitery() {
  const input = "TeST nAPIsu";
  const expectedOutput = "TEST NAPISU";
  const output = zamienNaWielkieLitery(input);

  console.assert(
    output === expectedOutput,
    `Test nie powiódł się dla ${input}`
  );
  console.log("Test przeszedł pomyślnie");
}

function testZamienLitery() {
  const input = "TeST nAPIsu";
  const expectedOutput = "tEst NapIsU";
  const output = zamienLitery(input);

  console.assert(
    output === expectedOutput,
    `Test nie powiódł się dla ${input}`
  );
  console.log("Test przeszedł pomyślnie");
}

function main() {
  testZamienNaMaleLitery();
  testZamienNaWielkieLitery();
  testZamienLitery();
}

main();
