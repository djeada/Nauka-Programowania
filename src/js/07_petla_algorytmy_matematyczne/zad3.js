/*
Tytuł: Mnożenie i dzielenie.

Treść: Napisz funkcję, która dla otrzymanych dwóch liczb naturalnych a i b, przy pomocy dodawania lub odejmowania oraz pętli, obliczy:

a) iloczyn tych liczb

b) iloraz liczby a przez liczbę b

Dane wejściowe: dwie liczby naturalne

Dane wyjściowe: liczba naturalna

Przykład:

Dla pobranych liczb 3 i 2, funkcja powinna zwrócić liczbę:

a) 6;

b) 2.
*/

// Funkcja zwracająca iloczyn dwóch liczb
function zwracajIloczynLiczb(liczba_a, liczba_b) {
  var wynik = 0;
  for (var i = 0; i < liczba_b; i++) {
    wynik += liczba_a;
  }
  return wynik;
}

// Funkcja zwracająca iloraz dwóch liczb
function zwracajIlorazLiczb(liczba_a, liczba_b) {
  if (liczba_b === 0) {
    return NaN;
  }

  var wynik = 0;
  while (liczba_a >= liczba_b) {
    liczba_a -= liczba_b;
    wynik++;
  }
  return wynik;
}

// Testy

function testIloczyn() {
  console.assert(zwracajIloczynLiczb(2, 3) == 6);
  console.assert(zwracajIloczynLiczb(3, 2) == 6);
  console.assert(zwracajIloczynLiczb(4, 4) == 16);
  console.assert(zwracajIloczynLiczb(5, 3) == 15);
  console.assert(zwracajIloczynLiczb(6, 0) == 0);
  console.assert(zwracajIloczynLiczb(7, 1) == 7);
  console.assert(zwracajIloczynLiczb(0, 2) == 0);
}

function testIloraz() {
  console.assert(zwracajIlorazLiczb(2, 3) == 0);
  console.assert(zwracajIlorazLiczb(3, 2) == 1);
  console.assert(zwracajIlorazLiczb(4, 4) == 1);
  console.assert(zwracajIlorazLiczb(5, 3) == 1);
  console.assert(Number.isNaN(zwracajIlorazLiczb(6, 0)));
  console.assert(zwracajIlorazLiczb(7, 1) == 7);
  console.assert(zwracajIlorazLiczb(0, 2) == 0);
}

// Funkcja uruchamiająca testy
function main() {
  testIloczyn();
  testIloraz();
}

// Uruchomienie testów
main();
