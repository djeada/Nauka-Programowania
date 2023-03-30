/*
Tytul: Znaki znajdujace sie na pozycjach bedacych liczbami pierwszymi.

Tresc: Otrzymasz napis. Znajdz znaki znajdujace sie na pozycjach bedacych liczbami pierwszymi.

Dane wejsciowe: Napis.

Dane wyjsciowe: Lista znakow.

Przyklad:

Dla otrzymanego napisu: "Slon", powinna zostac zwrocona lista: ['o', 'n'].
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
  let input = "Slon";
  let expectedOutput = ["o", "n"];
  let output = znakiNaPozycjachPierwszych(input);

  console.assert(
    JSON.stringify(output) === JSON.stringify(expectedOutput),
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

