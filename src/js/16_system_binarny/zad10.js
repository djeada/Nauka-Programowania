/*

Tytul: Zamien A na B.

Tresc: Otrzymujesz dwie liczby naturalne. Oblicz, ile bitow nalezy odwrocic, aby zamienic liczbe A na liczbe B.

Dane wejsciowe: Dwie liczby naturalne.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanych liczb 34 i 73, powinna zostac zwrocona liczba 5.*/

function zamien(a, b) {
  let wynik = 0;
  let xor = a ^ b;
  while (xor != 0) {
    wynik += xor & 1;
    xor >>= 1;
  }
  return wynik;
}

function test() {
  console.assert(zamien(34, 73) === 5, "Test 1 nie powiodl sie");
  console.assert(zamien(1, 1) === 0, "Test 2 nie powiodl sie");
  console.assert(zamien(0, 0) === 0, "Test 3 nie powiodl sie");
  console.assert(zamien(0, 1) === 1, "Test 4 nie powiodl sie");
  console.assert(zamien(1, 0) === 1, "Test 5 nie powiodl sie");
}

test();

