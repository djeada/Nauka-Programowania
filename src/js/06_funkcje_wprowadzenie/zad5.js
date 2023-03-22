/*
Tytuł: Zamień wartości miejscami.

Treść: Napisz funkcję, która zamieni wartości zmiennych a i b miejscami. Po wykonaniu funkcji zmienna a powinna przechowywać wartość zmiennej b, a zmienna b powinna przechowywać wartość zmiennej a.

Dane wejściowe: Dwie liczby naturalne.

Dane wyjściowe: Dwie liczby naturalne.

Przykład:

Dla otrzymanych liczb: 8 i 5, powinny zostać zwrócone liczby 5 i 8.
*/

// Funkcja zamieniająca wartości zmiennych
function zamienWartosciMiejscami(liczba_a, liczba_b) {
  let a = liczba_a;
  let b = liczba_b;
  let c = a;
  a = b;
  b = c;
  return [a, b];
}

// Pobieranie danych od użytkownika
const a = parseInt(prompt("Podaj liczbę a:"));
const b = parseInt(prompt("Podaj liczbę b:"));

// Wywołanie funkcji
const wynik = zamienWartosciMiejscami(a, b);

// Wyświetlanie wyniku
console.log(wynik);
