/*
Tytul: Napis skladajacy sie z liczb od 1 do n.

Tresc: Otrzymasz liczbe naturalna n. Zwroc napis skladajacy sie z liczb naturalnych od 1 do n.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Napis.

Przyklad:

Dla otrzymanej liczby n rownej 3 powinien zostac zwrocony napis: "123".
*/

function napisOd1DoN(n) {
  let wynik = "";
  for (let i = 1; i <= n; i++) {
    wynik += i;
  }
  return wynik;
}

// Test

function test() {
  let input = 3;
  let expectedOutput = "123";
  let output = napisOd1DoN(input);

  console.assert(
    output === expectedOutput,
    "Test nie powiodl sie dla " +
      input +
      ". Otrzymany wynik to " +
      output +
      ", a oczekiwany wynik to " +
      expectedOutput
  );
  console.log("Test przeszedl pomyslnie");
}

test();

