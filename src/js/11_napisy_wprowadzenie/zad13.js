/*
Tytuł: Znaki znajdujące się na pozycjach będących liczbami pierwszymi.

Treść: Otrzymasz napis. Znajdź znaki znajdujące się na pozycjach będących liczbami pierwszymi.

Dane wejściowe: Napis.

Dane wyjściowe: Lista znaków.

Przykład:

Dla otrzymanego napisu: "Słoń", powinna zostać zwrócona lista: ['o', 'ń'].
*/

function czyLiczbaPierwsza(n) {
  if (n < 2) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}

function znakiNaPozycjachPierwszych(napis) {
  let wynik = [];
  for (let i = 0; i < napis.length; i++) {
    if (czyLiczbaPierwsza(i)) {
      wynik.push(napis[i]);
    }
  }
  return wynik;
}

// Test

function test() {
  let input = "Słoń";
  let expectedOutput = ["o", "ń"];
  let output = znakiNaPozycjachPierwszych(input);

  assert(
    JSON.stringify(output) === JSON.stringify(expectedOutput),
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
