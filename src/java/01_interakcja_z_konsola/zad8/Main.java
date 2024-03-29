/*
Tytul: Obliczenie ceny podlogi.
Tresc: Otrzymasz cene pojedynczej plytki, wymiary plytki w postaci kwadratu oraz wymiary podlogi w postaci prostokata. Oblicz, ile kosztowac bedzie podloga o podanych wymiarach.
Jednostki sa umowne.
Dane wejsciowe: Cztery liczby naturalne: cena plytki, dlugosc boku plytki, dlugosc podlogi oraz szerokosc podlogi.
Dane wyjsciowe: Liczba naturalna oznaczajaca cene podlogi.
Przyklad:
Dla pobranych liczb: 2 (cena plytki), 3 (dlugosc boku plytki), 20 (dlugosc podlogi) oraz 40 (szerokosc podlogi), powinna zostac wypisana liczba: 196.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    System.out.print("podaj: cene plytki, dlugosc boku plytki i wymiary podlogi");
    System.out.print("\n");

    int cena;
    int bokPlytki;
    int szerokoscPodlogi;
    int dlugoscPodlogi;

    Scanner s = new Scanner(System.in);
    cena = Integer.parseInt(s.nextLine());
    bokPlytki = Integer.parseInt(s.nextLine());
    szerokoscPodlogi = Integer.parseInt(s.nextLine());
    dlugoscPodlogi = Integer.parseInt(s.nextLine());

    int szerokoscKonieczna = szerokoscPodlogi + bokPlytki - szerokoscPodlogi % bokPlytki;
    int dlugoscKonieczna = dlugoscPodlogi + bokPlytki - dlugoscPodlogi % bokPlytki;

    int polePlytki = (int) Math.pow(bokPlytki, 2);
    int polePodlogi = szerokoscKonieczna * dlugoscKonieczna;

    float calkowityKoszt = cena * (float) polePodlogi / polePlytki;

    System.out.print("Dla plytki o dlugosci boku " + bokPlytki + " i ceny " + cena);
    System.out.print(" calkowity koszt wylozenia podlogi o wymiarach " + szerokoscPodlogi);
    System.out.print("x" + dlugoscPodlogi + " wynosi " + calkowityKoszt + "\n");
  }
}

