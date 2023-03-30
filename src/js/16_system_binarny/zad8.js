/*
Tytuł: Najbliższa potęga dwójki.

Treść: Otrzymujesz reprezentację dziesiętną liczby naturalnej. Znajdź potęgę dwójki większą bądź równą tej liczbie. Inaczej: zaokrąglij liczbę do najbliższej potęgi dwójki.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej liczby: 111, powinna zostać zwrócona liczba: 128.*/

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
