/*
Tytul: Zamien wartosci miejscami.

Tresc: Napisz funkcje, ktora zamieni wartosci zmiennych a i b miejscami. Po wykonaniu funkcji zmienna a powinna przechowywac wartosc zmiennej b, a zmienna b powinna przechowywac wartosc zmiennej a.

Dane wejsciowe: Dwie liczby naturalne.

Dane wyjsciowe: Dwie liczby naturalne.

Przyklad:

Dla otrzymanych liczb: 8 i 5, powinny zostac zwrocone liczby 5 i 8.
*/

// Funkcja zamieniajaca wartosci zmiennych
function zamienWartosciMiejscami(liczba_a, liczba_b) {
  let a = liczba_a;
  let b = liczba_b;
  let c = a;
  a = b;
  b = c;
  return [a, b];
}

// Pobieranie danych od uzytkownika
const a = parseInt(prompt("Podaj liczbe a:"));
const b = parseInt(prompt("Podaj liczbe b:"));

// Wywolanie funkcji
const wynik = zamienWartosciMiejscami(a, b);

// Wyswietlanie wyniku
console.log(wynik);

