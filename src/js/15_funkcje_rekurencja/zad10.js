/*
Tytuł: Gra.	

Treść: W grze, w każdym ruchu gracz może zdobyć 3, 5 lub 10 punktów. Oblicz przy użyciu rekurencji, ile sposobów istnieje, aby gracz wygrał grę, gdy ma do dyspozycji N punktów.

Dane wejściowe: Liczba naturalna N.

Dane wyjściowe: Liczba naturalna.

Przykład:
Dla N = 20, powinna zostać zwrócona liczba: 4.

*/

function liczbaSposobowWygranej(n) {
  if (n === 0) {
    return 1;
  }
  if (n < 0) {
    return 0;
  }
  return (
    liczbaSposobowWygranej(n - 3) +
    liczbaSposobowWygranej(n - 5) +
    liczbaSposobowWygranej(n - 10)
  );
}

function assert(warunek, komunikat) {
  if (!warunek) {
    throw komunikat || "Wystąpił błąd";
  }
}

// Testy
function testLiczbaSposobowWygranej() {
  let n;
  let wynik;

  n = 6;
  wynik = liczbaSposobowWygranej(n);
  assert(wynik === 2, "Test 1 nieudany");

  n = 10;
  wynik = liczbaSposobowWygranej(n);
  assert(wynik === 2, "Test 2 nieudany");

  n = 20;
  wynik = liczbaSposobowWygranej(n);
  assert(wynik === 4, "Test 3 nieudany");

  n = 25;
  wynik = liczbaSposobowWygranej(n);
  assert(wynik === 5, "Test 4 nieudany");
}

testLiczbaSposobowWygranej();
console.log("Wszystkie testy zakończone sukcesem");
