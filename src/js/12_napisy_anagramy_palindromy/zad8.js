/*

Tytuł: Wyjątkowe palindromy.

Treść: Napisz program, który znajdzie wszystkie wyjątkowe palindromy, jakie można utworzyć ze znaków w słowie (bez zmiany kolejności występowania). Nie uwzględniaj duplikatów w liście.

Wyjątkowy palindrom musi spełniać jeden z dwóch warunków:

1. Wszystkie znaki są identyczne, np. “xxx”.
2. Wszystkie znaki poza środkowym znakiem są identyczne, np. “ccdcc”.

Pojedynczy znak jest również uznawany za wyjątkowy palindrom.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu: “xxxx”, powinna zostać zwrócona lista: [“x”, “xx”, 'xxx', 'xxxx'].
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
    'Test nie powiódł się dla "' +
      input +
      '". Otrzymany wynik to ' +
      JSON.stringify(output) +
      ", a oczekiwany wynik to " +
      JSON.stringify(expectedOutput)
  );
  console.log("Test przeszedł pomyślnie");
}

test();
