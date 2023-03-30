/*
Tytul: Czy liczba jest poprawnym numerem dnia tygodnia lub miesiaca?
Tresc: Wypisz pobrana od uzytkownika liczbe naturalna, jesli jest ona poprawnym numerem dnia tygodnia lub miesiaca.
Dane wejsciowe: Liczba naturalna.
Dane wyjsciowe: Liczba naturalna.
Przyklad:
* Dla pobranej liczby: 10, powinna zostac wypisana liczba: 10.
* Dla pobranej liczby: 15, nie powinna byc wypisana zadna liczba.

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Czy liczba jest numerem tygodnia/miesiaca?

    System.out.print("Podaj liczbe:\n");
    Scanner s = new Scanner(System.in);
    int a = Integer.parseInt(s.nextLine());

    if (a >= 1 && a <= 7) {
      System.out.print("Liczba jest poprawnym numerem tygodnia\n");
    } else {
      System.out.print("Liczba nie jest poprawnym numerem tygodnia\n");
    }

    if (a >= 1 && a <= 12) {
      System.out.print("Liczba jest poprawnym numerem miesiaca\n");
    } else {
      System.out.print("Liczba nie jest poprawnym numerem miesiaca\n");
    }
  }
}

