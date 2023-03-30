/*

Tytul: Wyszukanie wszystkich palindromow w zdaniu.

Tresc: Napisz program, ktory otrzymuje napis reprezentujacy zdanie. Twoim zadaniem jest znalezienie wszystkich palindromow w zdaniu. Roznice miedzy wielkimi i malymi literami powinny byc zignorowane.

Dane wejsciowe: Napis.

Dane wyjsciowe: Lista napisow.

Przyklad:

Dla otrzymanego napisu: “Tata zabral kajak na wycieczke i uderzyl sie w oko”, powinna zostac zwrocona lista: ["kajak", "i", "w", "oko"].
*/

function czyPalindrom(napis) {
  const napisBezSpacji = napis.replace(/\s/g, "");
  const odwroconyNapis = napisBezSpacji.split("").reverse().join("");
  return napisBezSpacji.toLowerCase() === odwroconyNapis.toLowerCase();
}

function wyszukajPalindromy(zdanie) {
  const slowa = zdanie.split(" ");
  const palindromy = [];

  for (const slowo of slowa) {
    if (czyPalindrom(slowo)) {
      palindromy.push(slowo);
    }
  }

  return palindromy;
}

// Test

function test() {
  const input = "Tata zabral kajak na wycieczke i uderzyl sie w oko";
  const expectedOutput = ["kajak", "i", "w", "oko"];
  const output = wyszukajPalindromy(input);

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

