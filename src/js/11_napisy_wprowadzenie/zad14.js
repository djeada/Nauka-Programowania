/*
Tytuł: Napis składający się z liczb od 1 do n.

Treść: Otrzymasz liczbę naturalną n. Zwróć napis składający się z liczb naturalnych od 1 do n.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanej liczby n równej 3 powinien zostać zwrócony napis: "123".
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

  assert(
    output === expectedOutput,
    "Test nie powiódł się dla " +
      input +
      ". Otrzymany wynik to " +
      output +
      ", a oczekiwany wynik to " +
      expectedOutput
  );
  console.log("Test przeszedł pomyślnie");
}

function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}

test();
