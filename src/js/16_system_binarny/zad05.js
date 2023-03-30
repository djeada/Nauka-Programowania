/*

Tytul: Wybieranie minimum i maksimum.

Tresc: Otrzymujesz dwie liczby naturalne.

a) Zwroc mniejsza z nich. Zabronione jest uzycie instrukcji warunkowej oraz zewnetrznych bibliotek.

b) Zwroc wieksza z nich. Zabronione jest uzycie instrukcji warunkowej oraz zewnetrznych bibliotek.

Dane wejsciowe: Dwie liczby naturalne w obu podpunktach.

Dane wyjsciowe: Liczba naturalna w obu podpunktach.

Przyklad:

a) Dla otrzymanych liczb: 3 i 2, powinna zostac zwrocona liczba: 2.

b) Dla otrzymanych liczb: 3 i 2, powinna zostac zwrocona liczba: 3.
*/

// Funkcja zwracajaca mniejsza z dwoch liczb
function minimum(a, b) {
  return (a + b - Math.abs(a - b)) / 2;
}

// Funkcja zwracajaca wieksza z dwoch liczb
function maximum(a, b) {
  return (a + b + Math.abs(a - b)) / 2;
}

function test() {
  console.assert(minimum(3, 2) === 2, "Test 1 nie powiodl sie");
  console.assert(maximum(3, 2) === 3, "Test 2 nie powiodl sie");
  console.assert(minimum(5, 5) === 5, "Test 3 nie powiodl sie");
  console.assert(maximum(5, 5) === 5, "Test 4 nie powiodl sie");
}

test();

