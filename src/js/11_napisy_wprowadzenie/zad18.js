/*
Tytuł: Odwróć słowa w zdaniu.

Treść: Otrzymujesz napis reprezentujący zdanie. Zamień słowa zdania na te same napisy zapisane wspak. Znaki interpunkcyjne nie są uwzględniane jako słowa.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanego napisu: "Ala ma kota", powinien zostać zwrócony napis: "ala mak otak".
*/

function rozbijNaSłowa(napis) {
  return napis.split(/[^\w]+/);
}

function odwróćSłowo(słowo) {
  return słowo.split("").reverse().join("");
}

function odwróćSłowa(napis) {
  let słowa = rozbijNaSłowa(napis);
  let wynik = [];
  for (let i = 0; i < słowa.length; i++) {
    if (słowa[i] !== "") {
      wynik.push(odwróćSłowo(słowa[i]));
    }
  }
  return wynik.join(" ");
}

// Test

function test() {
  let input = "Ala ma kota";
  let expectedOutput = "ala mak otak";
  let output = odwróćSłowa(input);

  assert(
    output === expectedOutput,
    'Test nie powiódł się dla "' +
      input +
      '". Otrzymany wynik to "' +
      output +
      '", a oczekiwany wynik to "' +
      expectedOutput +
      '"'
  );
  console.log("Test przeszedł pomyślnie");
}

function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}

test();
