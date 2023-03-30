/*

Tytul: Zmiana wielkosci liter.

Tresc: Otrzymujesz napis. Zaimplementuj nastepujace operacje przy uzyciu operatorow bitowych:

a) Zamien wielkie litery na male litery.

b) Zamien male litery na wielkie litery.

c) Zamien male litery na wielkie litery i wielkie litery na male litery.

Dane wejsciowe: Napis.

Dane wyjsciowe: Napis.

Przyklad:

a) Dla otrzymanego napisu: "Test", powinien zostac zwrocony napis: "test".

b) Dla otrzymanego napisu: "Test", powinien zostac zwrocony napis: "TEST".

c) Dla otrzymanego napisu: "Test", powinien zostac zwrocony napis: "tEST".
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
    `Test nie powiodl sie dla ${input}`
  );
  console.log("Test przeszedl pomyslnie");
}

function testZamienNaWielkieLitery() {
  const input = "TeST nAPIsu";
  const expectedOutput = "TEST NAPISU";
  const output = zamienNaWielkieLitery(input);

  console.assert(
    output === expectedOutput,
    `Test nie powiodl sie dla ${input}`
  );
  console.log("Test przeszedl pomyslnie");
}

function testZamienLitery() {
  const input = "TeST nAPIsu";
  const expectedOutput = "tEst NapIsU";
  const output = zamienLitery(input);

  console.assert(
    output === expectedOutput,
    `Test nie powiodl sie dla ${input}`
  );
  console.log("Test przeszedl pomyslnie");
}

function main() {
  testZamienNaMaleLitery();
  testZamienNaWielkieLitery();
  testZamienLitery();
}

main();

