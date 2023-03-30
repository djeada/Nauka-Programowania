/*
Tytul: Liczby z okreslonego przedzialu.

Tresc: Dla otrzymanych dwoch liczb naturalnych wypisz:

a) Wszystkie liczby naturalne wieksze od mniejszej otrzymanej liczby i jednoczesnie mniejsze od wiekszej otrzymanej liczby.

b) Wszystkie liczby naturalne podzielne przez 3 wieksze od mniejszej otrzymanej liczby i jednoczesnie mniejsze od wiekszej otrzymanej liczby.

Dane wejsciowe: Dwie liczby naturalne.

Dane wyjsciowe: Kilka liczb naturalnych.

Przyklad:

Dla otrzymanych liczb 9 i 5 powinny zostac wypisane liczby 6, 7 i 8.
*/

// Pobieranie danych od uzytkownika
const liczba_a = parseInt(prompt("Podaj pierwsza liczbe:"));
const liczba_b = parseInt(prompt("Podaj druga liczbe:"));

// Porownanie ze zmienna
const min = Math.min(liczba_a, liczba_b);
const max = Math.max(liczba_a, liczba_b);

// Petla
for (let i = min + 1; i < max; i++) {
  console.log(i);
}

// Petla
for (let i = min + 1; i < max; i++) {
  if (i % 3 === 0) {
    console.log(i);
  }
}

