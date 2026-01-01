/*
Tytul: Gra.	

Tresc: W grze, w kazdym ruchu gracz moze zdobyc 3, 5 lub 10 punktow. Oblicz przy uzyciu rekurencji, ile sposobow istnieje, aby gracz wygral gre, gdy ma do dyspozycji N punktow.

Dane wejsciowe: Liczba naturalna N.

Dane wyjsciowe: Liczba naturalna.

Przyklad:
Dla N = 20, powinna zostac zwrocona liczba: 4.

*/

// Funkcja oblicza liczbę sposobów (nieuporządkowanych) osiągnięcia n punktów
// Złożoność czasowa: O(n) z memoizacją
// Złożoność pamięciowa: O(n)
function liczbaSposobowWygranej(n, minRuch = 3, memo = {}) {
  if (n === 0) return 1;
  if (n < 0) return 0;
  
  const klucz = `${n},${minRuch}`;
  if (klucz in memo) return memo[klucz];
  
  let sposoby = 0;
  
  // Aby uniknąć powtórzeń, używamy tylko ruchów >= minRuch
  if (minRuch <= 3 && n >= 3) {
    sposoby += liczbaSposobowWygranej(n - 3, 3, memo);
  }
  if (minRuch <= 5 && n >= 5) {
    sposoby += liczbaSposobowWygranej(n - 5, 5, memo);
  }
  if (minRuch <= 10 && n >= 10) {
    sposoby += liczbaSposobowWygranej(n - 10, 10, memo);
  }
  
  memo[klucz] = sposoby;
  return sposoby;
}

// Testy
function testLiczbaSposobowWygranej() {
  let n;
  let wynik;

  n = 6;
  wynik = liczbaSposobowWygranej(n);
  console.assert(wynik === 1, "Test 1 nieudany"); // Tylko 3+3

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
console.log("Wszystkie testy zakończone sukcesem");

