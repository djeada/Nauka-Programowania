/*

Tytuł: Wyszukanie wszystkich palindromów w zdaniu.

Treść: Napisz program, który otrzymuje napis reprezentujący zdanie. Twoim zadaniem jest znalezienie wszystkich palindromów w zdaniu. Różnice między wielkimi i małymi literami powinny być zignorowane.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu: “Tata zabral kajak na wycieczke i uderzyl sie w oko”, powinna zostać zwrócona lista: ["kajak", "i", "w", "oko"].
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
