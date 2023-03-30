/*
Tytul:  Sprawdz warunek

Napisz funkcje, ktora sprawdzi nastepujace warunki dla otrzymanych dwoch liczb:

a) Czy pierwsza liczba jest wieksza od drugiej liczby?

b) Czy suma liczb jest mniejsza niz 10?

c) Czy obie liczby sa nieparzyste?

d) Czy wieksza liczba jest mniejsza od pierwszej liczby podniesionej do kwadratu?

Dane wejsciowe: dwie liczby naturalne

Dane wyjsciowe: cztery wartosci logiczne, odpowiadajace na kazde z pytan

Przyklad:

Dla pobranych liczb 3 i 2, funkcja powinna zwrocic nastepujace wartosci logiczne:

a) Prawda

b) Prawda

c) Falsz

d) Prawda
*/

// Funkcja sprawdzajaca czy pierwsza liczba jest wieksza od drugiej
function czyPierwszaWiekszaOdDrugiej(liczba_a, liczba_b) {
  return liczba_a > liczba_b;
}

// Funkcja sprawdzajaca czy suma liczb jest mniejsza niz 10
function czySumaMniejszaOd10(liczba_a, liczba_b) {
  return liczba_a + liczba_b < 10;
}

// Funkcja sprawdzajaca czy obie liczby sa nieparzyste
function czyObieNieparzyste(liczba_a, liczba_b) {
  return liczba_a % 2 !== 0 && liczba_b % 2 !== 0;
}

// Funkcja sprawdzajaca czy wieksza liczba jest mniejsza od pierwszej liczby podniesionej do kwadratu
function czyWiekszaMniejszaOdPierwszejDoKwadratu(liczba_a, liczba_b) {
  return Math.max(liczba_a, liczba_b) < Math.pow(liczba_a, 2);
}

// Pobieranie danych od uzytkownika
var liczba_a = parseInt(prompt("Podaj pierwsza liczbe:"));
var liczba_b = parseInt(prompt("Podaj druga liczbe:"));

// Wyswietlanie wynikow
console.log(
  "Czy pierwsza liczba jest wieksza od drugiej liczby? " +
    czyPierwszaWiekszaOdDrugiej(liczba_a, liczba_b)
);
console.log(
  "Czy suma liczb jest mniejsza niz 10? " +
    czySumaMniejszaOd10(liczba_a, liczba_b)
);
console.log(
  "Czy obie liczby sa nieparzyste? " + czyObieNieparzyste(liczba_a, liczba_b)
);
console.log(
  "Czy wieksza liczba jest mniejsza od pierwszej liczby podniesionej do kwadratu? " +
    czyWiekszaMniejszaOdPierwszejDoKwadratu(liczba_a, liczba_b)
);

