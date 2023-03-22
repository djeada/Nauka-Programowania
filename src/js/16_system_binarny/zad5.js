/*

Tytuł: Wybieranie minimum i maksimum.

Treść: Otrzymujesz dwie liczby naturalne.

a) Zwróć mniejszą z nich. Zabronione jest użycie instrukcji warunkowej oraz zewnętrznych bibliotek.

b) Zwróć większą z nich. Zabronione jest użycie instrukcji warunkowej oraz zewnętrznych bibliotek.

Dane wejściowe: Dwie liczby naturalne w obu podpunktach.

Dane wyjściowe: Liczba naturalna w obu podpunktach.

Przykład:

a) Dla otrzymanych liczb: 3 i 2, powinna zostać zwrócona liczba: 2.

b) Dla otrzymanych liczb: 3 i 2, powinna zostać zwrócona liczba: 3.
*/

// Funkcja zwracająca mniejszą z dwóch liczb
function minimum(a, b) {
  return (a + b - Math.abs(a - b)) / 2;
}

// Funkcja zwracająca większą z dwóch liczb
function maximum(a, b) {
  return (a + b + Math.abs(a - b)) / 2;
}

// Testy
function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
}

function test() {
  assert(minimum(3, 2) === 2, "Test 1 nie powiódł się");
  assert(maximum(3, 2) === 3, "Test 2 nie powiódł się");
  assert(minimum(5, 5) === 5, "Test 3 nie powiódł się");
  assert(maximum(5, 5) === 5, "Test 4 nie powiódł się");
}

test();
