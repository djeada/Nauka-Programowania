/*
Tytuł: Operacje arytmetyczne.

Treść: Napisz funkcję, która dla otrzymanych dwóch liczb zwróci:

a) Ich sumę.

b) Różnicę drugiej i pierwszej.

c) Ich iloczyn.

d) Iloraz pierwszej przez drugą.

e) Resztę z dzielenia pierwszej przez drugą.

Dane wejściowe: Dwie liczby naturalne dla wszystkich podpunktów.

Dane wyjściowe: Liczba całkowita dla wszystkich podpunktów.

Przykład:

Dla pobranych liczb: 3 i 5, funkcja powinna zwrócić:

a) Sumę: 8

b) Różnicę: 2

c) Iloczyn: 15

d) Iloraz: 0

e) Resztę z dzielenia: 3
*/

// Funkcja zwracająca sumę
function zwracajSuma(liczba_a, liczba_b) {
  return liczba_a + liczba_b;
}

// Funkcja zwracająca różnicę
function zwracajRoznica(liczba_a, liczba_b) {
  return liczba_b - liczba_a;
}

// Funkcja zwracająca iloczyn
function zwracajIloczyn(liczba_a, liczba_b) {
  return liczba_a * liczba_b;
}

// Funkcja zwracająca iloraz
function zwracajIloraz(liczba_a, liczba_b) {
  return liczba_a / liczba_b;
}

// Funkcja zwracająca resztę z dzielenia
function zwracajReszteZDzielenia(liczba_a, liczba_b) {
  return liczba_a % liczba_b;
}

// Pobieranie danych od użytkownika
const liczba_a = parseInt(prompt("Podaj pierwszą liczbę:"));
const liczba_b = parseInt(prompt("Podaj drugą liczbę:"));

// Wywołanie funkcji
console.log("Suma: " + zwracajSuma(liczba_a, liczba_b));
console.log("Różnica: " + zwracajRoznica(liczba_a, liczba_b));
console.log("Iloczyn: " + zwracajIloczyn(liczba_a, liczba_b));
console.log("Iloraz: " + zwracajIloraz(liczba_a, liczba_b));
console.log(
  "Reszta z dzielenia: " + zwracajReszteZDzielenia(liczba_a, liczba_b)
);
