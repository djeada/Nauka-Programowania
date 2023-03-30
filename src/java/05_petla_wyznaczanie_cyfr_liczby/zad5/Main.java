/*
Czy liczba jest palindromem?
Tresc: Dla otrzymanej liczby naturalnej sprawdz, czy jest ona palindromem, tj. czy nie zmienia sie po zapisaniu cyfr w odwrotnej kolejnosci.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Komunikat.
Przyklad:
Dla otrzymanej liczby 13231, powinna zostac wypisana informacja o tym, ze liczba jest palindromem.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Dla pobranej liczby, sprawdz czy jest palindromem.

    System.out.print("Podaj liczbe\n");
    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());

    int odwrocona = 0;
    int pom = a;

    while (pom > 0) {
      int cyfra = pom % 10;
      odwrocona = (odwrocona * 10 + cyfra);
      pom /= 10;
    }

    if (odwrocona == a) {
      System.out.print("podana liczba jest palindromem\n");
    } else {
      System.out.print("podana liczba nie jest palindromem\n");
    }
  }
}

