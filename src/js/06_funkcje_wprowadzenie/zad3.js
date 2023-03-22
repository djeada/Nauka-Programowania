/*
Tytuł:  Sprawdź warunek

Napisz funkcję, która sprawdzi następujące warunki dla otrzymanych dwóch liczb:

a) Czy pierwsza liczba jest większa od drugiej liczby?

b) Czy suma liczb jest mniejsza niż 10?

c) Czy obie liczby są nieparzyste?

d) Czy większa liczba jest mniejsza od pierwszej liczby podniesionej do kwadratu?

Dane wejściowe: dwie liczby naturalne

Dane wyjściowe: cztery wartości logiczne, odpowiadające na każde z pytań

Przykład:

Dla pobranych liczb 3 i 2, funkcja powinna zwrócić następujące wartości logiczne:

a) Prawda

b) Prawda

c) Fałsz

d) Prawda
*/

// Funkcja sprawdzająca czy pierwsza liczba jest większa od drugiej
function czyPierwszaWiekszaOdDrugiej(liczba_a, liczba_b) {
  return liczba_a > liczba_b;
}

// Funkcja sprawdzająca czy suma liczb jest mniejsza niż 10
function czySumaMniejszaOd10(liczba_a, liczba_b) {
  return liczba_a + liczba_b < 10;
}

// Funkcja sprawdzająca czy obie liczby są nieparzyste
function czyObieNieparzyste(liczba_a, liczba_b) {
  return liczba_a % 2 !== 0 && liczba_b % 2 !== 0;
}

// Funkcja sprawdzająca czy większa liczba jest mniejsza od pierwszej liczby podniesionej do kwadratu
function czyWiekszaMniejszaOdPierwszejDoKwadratu(liczba_a, liczba_b) {
  return Math.max(liczba_a, liczba_b) < Math.pow(liczba_a, 2);
}

// Pobieranie danych od użytkownika
var liczba_a = parseInt(prompt("Podaj pierwszą liczbę:"));
var liczba_b = parseInt(prompt("Podaj drugą liczbę:"));

// Wyświetlanie wyników
console.log(
  "Czy pierwsza liczba jest większa od drugiej liczby? " +
    czyPierwszaWiekszaOdDrugiej(liczba_a, liczba_b)
);
console.log(
  "Czy suma liczb jest mniejsza niż 10? " +
    czySumaMniejszaOd10(liczba_a, liczba_b)
);
console.log(
  "Czy obie liczby są nieparzyste? " + czyObieNieparzyste(liczba_a, liczba_b)
);
console.log(
  "Czy większa liczba jest mniejsza od pierwszej liczby podniesionej do kwadratu? " +
    czyWiekszaMniejszaOdPierwszejDoKwadratu(liczba_a, liczba_b)
);
