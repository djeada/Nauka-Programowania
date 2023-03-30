/*
Tytul: Odwroc slowa w zdaniu.
Tresc: Otrzymujesz napis reprezentujacy zdanie. Zamien slowa zdania na te same napisy zapisane wspak. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.
Dane wejsciowe: Napis.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanego napisu: "Ala ma kota", powinien zostac zwrocony napis: "ala mak otak".

*/
import java.util.*;

public class Main {
  // Otrzymujesz rekord z bazy danych reprezentujacy dane pracownika.
  // Sa to kolejno: imie, nazwisko, miejsce urodzenia, stanowisko i zarobki.
  // Informacje rozdzielone sa srednikami. Zapisz je w osobnych zmiennych
  // i wypisz wraz z komunikatem.

  public static void wypiszDane(String napis) {

    ArrayList<String> wynik = new ArrayList<String>(Arrays.asList(napis.split(";")));
    assert wynik.size() == 5;

    System.out.print("Imie: " + wynik.get(0) + "\n");
    System.out.print("Nazwisko: " + wynik.get(1) + "\n");
    System.out.print("Miejsce urodzenia: " + wynik.get(2) + "\n");
    System.out.print("Zawod: " + wynik.get(3) + "\n");
    System.out.print("Zarobki: " + wynik.get(4) + "\n");
  }

  public static void main(String[] args) {
    String napis = "Jan; Kowalski; Warszawa; Programista; 1000";
    wypiszDane(napis);
  }
}

