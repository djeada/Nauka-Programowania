/*
Tytuł: Liczby z określonego przedziału.

Treść: Dla otrzymanych dwóch liczb naturalnych wypisz:

a) Wszystkie liczby naturalne większe od mniejszej otrzymanej liczby i jednocześnie mniejsze od większej otrzymanej liczby.

b) Wszystkie liczby naturalne podzielne przez 3 większe od mniejszej otrzymanej liczby i jednocześnie mniejsze od większej otrzymanej liczby.

Dane wejściowe: Dwie liczby naturalne.

Dane wyjściowe: Kilka liczb naturalnych.

Przykład:

Dla otrzymanych liczb 9 i 5 powinny zostać wypisane liczby 6, 7 i 8.
*/

// Pobieranie danych od użytkownika
const liczba_a = parseInt(prompt("Podaj pierwszą liczbę:"));
const liczba_b = parseInt(prompt("Podaj drugą liczbę:"));

// Porównanie ze zmienną
const min = Math.min(liczba_a, liczba_b);
const max = Math.max(liczba_a, liczba_b);

// Pętla
for (let i = min + 1; i < max; i++) {
    console.log(i);
}

// Pętla
for (let i = min + 1; i < max; i++) {
    if (i % 3 === 0) {
        console.log(i);
    }
}