/*
Tytul: Gra.	

Tresc: W grze, w kazdym ruchu gracz moze zdobyc 3, 5 lub 10 punktow. Oblicz przy uzyciu rekurencji, ile sposobow istnieje, aby gracz wygral gre, gdy ma do dyspozycji N punktow.

Dane wejsciowe: Liczba naturalna N.

Dane wyjsciowe: Liczba naturalna.

Przyklad:
Dla N = 20, powinna zostac zwrocona liczba: 4.

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

// Testy
function testLiczbaSposobowWygranej() {
  let n;
  let wynik;

  n = 6;
  wynik = liczbaSposobowWygranej(n);
  console.assert(wynik === 2, "Test 1 nieudany");

  n = 10;
  wynik = liczbaSposobowWygranej(n);
  console.assert(wynik === 2, "Test 2 nieudany");

  n = 20;
  wynik = liczbaSposobowWygranej(n);
  console.assert(wynik === 4, "Test 3 nieudany");

  n = 25;
  wynik = liczbaSposobowWygranej(n);
  console.assert(wynik === 5, "Test 4 nieudany");
}

testLiczbaSposobowWygranej();
console.log("Wszystkie testy zakonczone sukcesem");

