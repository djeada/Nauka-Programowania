/*
Tytul: Operacje arytmetyczne.

Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb zwroci:

a) Ich sume.

b) Roznice drugiej i pierwszej.

c) Ich iloczyn.

d) Iloraz pierwszej przez druga.

e) Reszte z dzielenia pierwszej przez druga.

Dane wejsciowe: Dwie liczby naturalne dla wszystkich podpunktow.

Dane wyjsciowe: Liczba calkowita dla wszystkich podpunktow.

Przyklad:

Dla pobranych liczb: 3 i 5, funkcja powinna zwrocic:

a) Sume: 8

b) Roznice: 2

c) Iloczyn: 15

d) Iloraz: 0

e) Reszte z dzielenia: 3
*/

// Funkcja zwracajaca sume
function zwracajSuma(liczba_a, liczba_b) {
  return liczba_a + liczba_b;
}

// Funkcja zwracajaca roznice
function zwracajRoznica(liczba_a, liczba_b) {
  return liczba_b - liczba_a;
}

// Funkcja zwracajaca iloczyn
function zwracajIloczyn(liczba_a, liczba_b) {
  return liczba_a * liczba_b;
}

// Funkcja zwracajaca iloraz
function zwracajIloraz(liczba_a, liczba_b) {
  return liczba_a / liczba_b;
}

// Funkcja zwracajaca reszte z dzielenia
function zwracajReszteZDzielenia(liczba_a, liczba_b) {
  return liczba_a % liczba_b;
}

// Pobieranie danych od uzytkownika
const liczba_a = parseInt(prompt("Podaj pierwsza liczbe:"));
const liczba_b = parseInt(prompt("Podaj druga liczbe:"));

// Wywolanie funkcji
console.log("Suma: " + zwracajSuma(liczba_a, liczba_b));
console.log("Roznica: " + zwracajRoznica(liczba_a, liczba_b));
console.log("Iloczyn: " + zwracajIloczyn(liczba_a, liczba_b));
console.log("Iloraz: " + zwracajIloraz(liczba_a, liczba_b));
console.log(
  "Reszta z dzielenia: " + zwracajReszteZDzielenia(liczba_a, liczba_b)
);

