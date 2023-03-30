/*
Tytul: Napis skladajacy sie z liczb od 1 do n.
Tresc: Otrzymasz liczbe naturalna n. Zwroc napis skladajacy sie z liczb naturalnych od 1 do n.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Napis.
Przyklad:
Dla otrzymanej liczby n rownej 3 powinien zostac zwrocony napis: "123".

*/
import java.util.*;

public class Main {
  // Otrzymujesz napis oraz liczbe k.
  // a) wypisz poziomo co k-ty znak. Znaki powinny byc oddzielone spacjami.
  public static void wypiszPoziomo(final String napis, int k) {

    for (int i = 0; i < napis.length(); i += k) {
      System.out.print(napis.charAt(i));
      System.out.print(", ");
    }

    System.out.print("\n");
  }

  // b) wypisz pionowo co k-ty znak. Znaki powinny byc oddzielone enterami.
  public static void wypiszPionowo(final String napis, int k) {
    for (int i = 0; i < napis.length(); i += k) {
      System.out.print(napis.charAt(i));
      System.out.print("\n");
    }
  }

  public static void main(String[] args) {
    String napis = "hej dzieci jesli chcecie zobaczyc smerfow las";
    int k = 3;
    wypiszPoziomo(napis, k);
    wypiszPionowo(napis, k);
  }
}

