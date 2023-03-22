/*

Tytuł: Zamień A na B.

Treść: Otrzymujesz dwie liczby naturalne. Oblicz, ile bitów należy odwrócić, aby zamienić liczbę A na liczbę B.

Dane wejściowe: Dwie liczby naturalne.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanych liczb 34 i 73, powinna zostać zwrócona liczba 5.*/

function zamien(a, b) {
  let wynik = 0;
  let xor = a ^ b;
  while (xor != 0) {
    wynik += xor & 1;
    xor >>= 1;
  }
  return wynik;
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function test() {
  assert(zamien(34, 73) === 5, "Test 1 nie powiódł się");
  assert(zamien(1, 1) === 0, "Test 2 nie powiódł się");
  assert(zamien(0, 0) === 0, "Test 3 nie powiódł się");
  assert(zamien(0, 1) === 1, "Test 4 nie powiódł się");
  assert(zamien(1, 0) === 1, "Test 5 nie powiódł się");
}

test();
