/*
Tytul: Najblizsza potega dwojki.

Tresc: Otrzymujesz reprezentacje dziesietna liczby naturalnej. Znajdz potege dwojki wieksza badz rowna tej liczbie. Inaczej: zaokraglij liczbe do najblizszej potegi dwojki.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanej liczby: 111, powinna zostac zwrocona liczba: 128.*/

function najblizszaPotegaDwojki(n) {
  let potegaDwojki = 1;
  while (potegaDwojki < n) {
    potegaDwojki *= 2;
  }
  return potegaDwojki;
}

// Testy
function test() {
  const input = 111;
  const expectedOutput = 128;
  const output = najblizszaPotegaDwojki(input);
  console.assert(
    output === expectedOutput,
    "Dla ${input} otrzymano ${output}, oczekiwano ${expectedOutput}"
  );
  console.log("Test passed!");
}

test();

