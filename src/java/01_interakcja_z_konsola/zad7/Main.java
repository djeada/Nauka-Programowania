/*
Tytul: Pole powierzchni i objetosc figur geometrycznych.
Tresc zadania: Napisz program, ktory bedzie obliczal pola powierzchni i objetosci figur geometrycznych zgodnie z nastepujacymi instrukcjami:
a) Pobierz dlugosci podstawy i wysokosci trojkata i wypisz jego pole.
b) Pobierz dlugosci bokow prostokata i wypisz jego pole.
c) Pobierz dlugosci przekatnych rombu i wypisz jego pole.
d) Pobierz promien kuli i wypisz jej objetosc.
e) Pobierz promien podstawy i wysokosc stozka i wypisz jego objetosc.
f) Pobierz dlugosc, szerokosc i wysokosc graniastoslupa i wypisz jego objetosc.
Jednostki sa dowolne.
Dane wejsciowe:
* Dwie liczby naturalne dla podpunktow a, b i c.
* Liczba naturalna dla podpunktu d.
* Dwie liczby naturalne dla podpunktu e.
* Trzy liczby naturalne dla podpunktu f.
Dane wyjsciowe: Liczba naturalna dla wszystkich podpunktow.
Przyklad:
a) Dla pobranych liczb: 5 i 2, powinna zostac wypisana liczba: 5.
b) Dla pobranych liczb: 3 i 3, powinna zostac wypisana liczba: 4.
c) Dla pobranych liczb: 2 i 4, powinna zostac wypisana liczba: 1.
d) Dla pobranej liczby: 2, powinna zostac wypisana liczba: 33.493.
e) Dla pobranych liczb: 3 i 2, powinna zostac wypisana liczba: 18.84.
f) Dla pobranych liczb: 2, 2 i 2, powinny zostac wypisana liczba: 8.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {
    // Pobierz podstawe i wysokosc trojkata i wypisz pole.

    System.out.print("podaj podstawe i wysokosc trojkata: \n");

    Scanner s = new Scanner(System.in);

    float a = Float.parseFloat(s.nextLine());
    float h = Float.parseFloat(s.nextLine());

    System.out.print(
        "pole trojkata o podstawie "
            + a
            + " i wysokosci "
            + h
            + " jest rowne "
            + (a * h / 2)
            + "\n");

    // Pobierz dlogosci bokow prostokata i wypisz pole.

    System.out.print("podaj dlugosci bokow prostokata:\n");

    a = Float.parseFloat(s.nextLine());

    float b = Float.parseFloat(s.nextLine());

    System.out.print("pole prostokata o bokach " + a + " i " + b + " jest rowne " + (a * b) + "\n");
  }
}

