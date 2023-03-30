/*

Tytul: Wyjatkowe palindromy.

Tresc: Napisz program, ktory znajdzie wszystkie wyjatkowe palindromy, jakie mozna utworzyc ze znakow w slowie (bez zmiany kolejnosci wystepowania). Nie uwzgledniaj duplikatow w liscie.

Wyjatkowy palindrom musi spelniac jeden z dwoch warunkow:

1. Wszystkie znaki sa identyczne, np. “xxx”.
2. Wszystkie znaki poza srodkowym znakiem sa identyczne, np. “ccdcc”.

Pojedynczy znak jest rowniez uznawany za wyjatkowy palindrom.

Dane wejsciowe: Napis.

Dane wyjsciowe: Lista napisow.

Przyklad:

Dla otrzymanego napisu: “xxxx”, powinna zostac zwrocona lista: [“x”, “xx”, 'xxx', 'xxxx'].
*/

function czyWyjatkowyPalindrom(napis) {
  const srodek = Math.floor(napis.length / 2);
  const pierwszyZnak = napis[0];

  for (let i = 0; i < srodek; i++) {
    if (napis[i] !== pierwszyZnak) {
      return false;
    }
  }

  for (let i = srodek + 1; i < napis.length; i++) {
    if (napis[i] !== pierwszyZnak) {
      return false;
    }
  }

  return true;
}

function wyjatkowePalindromy(napis) {
  const wynik = new Set();

  for (let i = 0; i < napis.length; i++) {
    for (let j = i + 1; j <= napis.length; j++) {
      const podnapis = napis.slice(i, j);
      if (czyWyjatkowyPalindrom(podnapis)) {
        wynik.add(podnapis);
      }
    }
  }

  return Array.from(wynik);
}

// Test

function test() {
  const input = "xxxx";
  const expectedOutput = ["x", "xx", "xxx", "xxxx"];
  const output = wyjatkowePalindromy(input);

  console.assert(
    JSON.stringify(output) === JSON.stringify(expectedOutput),
    'Test nie powiodl sie dla "' +
      input +
      '". Otrzymany wynik to ' +
      JSON.stringify(output) +
      ", a oczekiwany wynik to " +
      JSON.stringify(expectedOutput)
  );
  console.log("Test przeszedl pomyslnie");
}

test();

